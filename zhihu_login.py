from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException

client = ZhihuClient()

try:
    client.login('#Email#', '#Password#')
except NeedCaptchaException:
    # ������֤�벢��ʾ���룬���µ�¼
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login('email_or_phone', 'password', captcha)

client.save_token('token.pkl')