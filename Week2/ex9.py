#JSON (JavaScript Object Notation)
import json

# json
# list, dict

a = [1,2,3,4]
aa = {
    "k0" : "v0",
    "k1" : "v2"
}

print(a[0])
b = json.dumps(a) # list(dict) => json(엄밀히 따지면 문자열))
print(b[0])
print(b)

bb = json.dumps(aa)
print(aa)
print(bb)

reverted = json.loads(bb) # json 문자열 => list, dict 변환
print(reverted)

# 네트워크 통신할 때 json을 많이 씀