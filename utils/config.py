############################ MOMO QUICK API URL ############################
# TEST
API_BASE_URL = "https://localhost:5000"
API_CLIENT_URL = "https://www.macross.kr"

# API_BASE_URL = "http://localhost:5002"
# API_CLIENT_URL = "http://localhost:82"

'''
# REAL
API_BASE_URL = "http://www.momoquick.com:5000"
API_CLIENT_URL = "http://www.momoquick.com"
'''
############################ DB INFO ############################

# # DEV DB - BETA
# DB_HOST = "localhost"
# DB_USR = "root"
# DB_PASSWORD = "mintquick"
# DB_DATABASE = "qdb"
# DB_PORT = 3306
'''
# DEV DB
DB_HOST = "qcluster.cluster-c4ijdhnilwqv.us-east-1.rds.amazonaws.com"
DB_USR = "admin"
DB_PASSWORD = "mintquick"
DB_DATABASE = "qdb"
DB_PORT = 3306
'''

'''
# REAL DB
DB_HOST = "quick-cluster-instance-1.cmvd8jvvxhjw.ap-northeast-2.rds.amazonaws.com"
DB_USR = "admin"
DB_PASSWORD = "mintquick"
DB_DATABASE = "qdb"
DB_PORT = 3306
'''
############################ NICEPAY INFO ############################

# 일반결제
# NICEPAY DEV
# MerchantKey = "EYzu8jGGMfqaDEp76gSckuvnaHHu+bC4opsSN6lHv3b2lurNYkVXrZ7Z1AoqQnXI3eLuaUFyoRNC6FkrzVjceg==" #상점키
# MID = "nicepay00m" # 상점아이디
# CancelPwd = "123456"  # 취소비밀번호

'''
# REAL (퀵돌이와 차돌이)
MerchantKey = "b5Q9gb1A2/Ozh7sHUnB/UazCwxhsM1gDFGExnqmb/gaMcgdUvP2Y33TNj8qSQQz3T1NVIbn/HVk2J/2Hecxrlw==" #상점키
MID = "thelight1m" # 상점아이디
CancelPwd = "thelight1"  # 취소비밀번호
'''

'''
# REAL (모모퀵물류)
MerchantKey = "OGL6JiMlZ3G64SECNjw7xoVU9xaum8jLToJ1UzIqRoBy6T4VVK3av1LB9useJSZgkDisNZkI7eHunPhbCWNJXQ==" #상점키
MID = "momoq0001m" # 상점아이디
CancelPwd = "momoq0001"  # 취소비밀번호
'''

# 간편결제
# BILL NICEPAY DEV
# BILL_MerchantKey = "b+zhZ4yOZ7FsH8pm5lhDfHZEb79tIwnjsdA0FBXh86yLc6BJeFVrZFXhAoJ3gEWgrWwN+lJMV0W4hvDdbe4Sjw==" #상점키
# BILL_MID = "nictest04m" # 상점아이디
'''
# REAL BILL
BILL_MerchantKey = "FB+DbFIsOKnZgXHT5TUnOG59Ksg4V+UZG1BcJzmflkAb2AkVwOIpBkiKr5lPZSxvhwow+tAoqzL2pNH0Rvsd5Q==" #상점키
BILL_MID = "momoq0002m" # 상점아이디
'''

# BILL CIPHER_KEY
# BILL_CIPHER_KEY = 'adaf729ccf3611ecaf93283a4d155c2e'
#
# ############################ ETC ############################
# JANDI_DEFAULT_URL = 'https://wh.jandi.com/connect-api/webhook/26485552/36364aefc26863e90a91a7bd656d0a59'

############################ Insung Info ############################
#모모퀵
# INSUNG_M_CODE = 6477      # 모모퀵 M_CODE
# INSUNG_CC_CODE = 11624    # 모모퀵 CC_CODE
# INSUNG_UKEY = '12345678f3a725be5b5ad5676fdd55b3046342cc'
# INSUNG_AKEY = 'dfa8a0973f7138730fb90fdbdb9c5881'
# INSUNG_USER_ID = 'momoquick'

# 모모퀵 물류
# INSUNG_M_CODE = 4559
# INSUNG_CC_CODE = 11690
# INSUNG_UKEY = '12345678af989e0f779ee27d0df884e41371dd99'
# INSUNG_AKEY = 'daf5293c5b2412a6d27a6d6754d5bb11'
# INSUNG_USER_ID = 'momoquick'

############################ Popbill Info ############################
# KAKAO
POPBILL_KAKAO_LINK_ID = 'LOGIALL'
POPBILL_KAKAO_SECRET_KEY = 'yMPUQX7mXDOkEnbOyErplv4qrheJ3oxupsTthx06gJg='

# SMS
# POPBILL_SMS_LINK_ID = 'LOGIALL'
# POPBILL_SMS_SECRET_KEY = 'yMPUQX7mXDOkEnbOyErplv4qrheJ3oxupsTthx06gJg='
#
# POPBILL_CORPNUM = '5738600351'
# POPBILL_USER_ID = 'sgdr8888'
# # POPBILL_SENDER = '16614030' # 모모퀵
# POPBILL_SENDER = '16440927' # 모모퀵물류
# POPBILL_SENDER_NAME = '모모퀵'

############################## DynamoDB / JWT Info ####################################
JWT_SECRET_KEY = "NGPGgy2IplUz3IMbf4f2tLZa5gD1KkdY"                      # JWT 암복호화 비밀키
DYNAMODB_TABLE_NAME = 'sd_connect'                                        # test서버 dynamoDB
DYNAMODB_REGION_NAME ='us-east-1'                                        # test서버 dynamoDB region
DYNAMODB_ACCESS_KEY_ID = 'AKIAX2OIAPJO75IVJSE2'                          # test서버 dynamoDB access key
DYNAMODB_SECRET_ACCESS_KEY = 'mQ4hIuHDaFkLTDD3EDvWu76aMLN4UqcEOf1AsStu'  # test서버 dynamoDB secret key

# DYNAMODB_TABLE_NAME = 'momoQuick'                                        # real서버 dynamoDB
# DYNAMODB_REGION_NAME ='ap-northeast-2'                                   # real서버 dynamoDB region
# DYNAMODB_ACCESS_KEY_ID = 'AKIATKY4QBVIPUH6DX75'                          # real서버 dynamoDB access key
# DYNAMODB_SECRET_ACCESS_KEY = 'xz8ROIRZy0GXMX8QdrV2eQvfp4BzKeg1KaKHOq6h'  # real서버 dynamoDB secret key

############################# hash info ################################
KEY_STRETCHING = 10  # 2의 10승만큼 해시 반복


############################# 신규가입 쿠폰코드 ###############################
NEW_MEMBER_COUPON_CD = "3f7e03af4dc8"
