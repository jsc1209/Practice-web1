import time
import pyupbit
import datetime

access = "UaRqY9LsAfkbqXMHWEcgs0e5ZHPFfX2GUFhTTITB"          # 본인 값으로 변경
secret = "X5MyxYM8YrpRpKvBvt8imOB0rYVll9WfzrZsnRvb"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회