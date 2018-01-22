from Contacts import Contact
import json

obj=Contact('홍길동','010-1811-2222','hong@naver.com')

d=obj.as_dict()

json_str=json.dumps(d)
print(json_str)

target=json.loads(json_str)
json_str=json.dumps(d,indent=4)
target=json.loads(json_str)
print(json_str)
print(target)



cls=target["__class__"]
cls=eval(cls)
print(type(cls))
print(cls)
args=target["__args__"]
print(type(args))
print(args)
kw=target["__kw__"]
print(type(kw))
print(kw)


print('-------------------')
contact=cls(**kw)
print(contact)
contact.print_detail()
print('-------------------------')