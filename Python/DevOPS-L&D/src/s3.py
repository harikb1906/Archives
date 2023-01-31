#!/usr/bin/env python
import boto3


def get_bucket_list():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket)


def get_bucket_objects(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.all():
        print(obj.key)


# get_bucket_list()
# get_bucket_objects('trainingpractice')


# str
name = 'inapp'
num = 2
flt = 2.0
arr = ['adfb', 1, 2.0, 45, 53]

# arr = ('adfb', 1, 2.0)
# arr[0] = 'shgjg'
# print(arr[1])

# Dict

dct = {
    "a": 55,
    "b": 2
}
# print(dct.get('a'))


st = {22, 'ass', 22}

a = 2
b = 3
c = 2

# if a == b:
#     print(True)
#     print("inside")
# elif b == 3:
#     print("b=3")
# else:
#     print(False)

# for i in arr:
#     print(i)

# i = 1
# while i < 6:
#   print(i)
#   i += 1

# arr = [1, 23, 54]
# for idx, el in enumerate(arr):
#     print(idx, el)

# print(arr[2])


# def my_fun(name, *args, **kwargs):
#     # print(args)
#     print(kwargs)
#     # print(name)

# my_fun("InAPp", "DevOPS", ids="sdhgsdjh")

# print(arr)
# arr.append(65)
# print(arr)
# arr.remove(53)
# print(arr)
# arr.pop(1)
# print(arr)


def user_name():
    username = input("What is your name? /n")
    print(username)

user_name()

