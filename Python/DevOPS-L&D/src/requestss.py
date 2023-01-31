#!/usr/bin/env python
import requests


def get_url(url, headers={}):
    r = requests.get(url, headers=headers)
    return r.status_code


# if __name__ == '__main__':
#     print(get_url('https://www.google.com/'))
    
    
class StudentName:
    a = 'a'

    @staticmethod
    def student_name(abc):
        return abc

print(StudentName.student_name("hjg"))