from email_osg.Requests import Request

RED = "\033[38;2;0;0;255m"
WHITE = "\033[37m"
GREEN = "\033[38;2;0;201;87m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
PURPLE = "\033[38;2;171;130;255m"
PINK = "\033[38;2;255;20;147m"
BLACK = "\033[38;2;89;89;89m"

async def instagram(target: str):
    # Step 1: Verify Request to Instagram's Signup Page
    req = await Request("https://www.instagram.com/accounts/emailsignup/").get()

    # Step 2: Retrieve and Validate Cookies
    try:
        csrf_token = req.cookies.get('csrftoken')
    except:
        print(f"{RED}>{WHITE} Instagram / Csrftoken not found")
        pass


    # Prepare data for the next request
    data = {
        'email': target,
        'first_name': '',
        'username': '',
        'opt_into_one_tap': False
    }

    # Step 3: Make the post request with the csrf_token
    r = await Request("https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/", headers={'x-csrftoken': csrf_token}, data=data).post()

    # Step 4: Handle response and possible errors
    try:
        code = r.json().get('errors', {}).get('email', [{}])[0].get('code')

        if code == 'email_is_taken':
            print(f"{GREEN}>{WHITE} Instagram")
        else:
            print(f"{RED}>{WHITE} Instagram")
    except (KeyError, IndexError) as e:
        print(f"{RED}>{WHITE} Instagram error: {str(e)}")
    except Exception as e:
        print(f"{RED}>{WHITE} Error: {str(e)}")
