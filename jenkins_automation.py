import jenkins
import json
import os

host = 'http://localhost:8080'
username = 'hardikshettyar'#'1188464bdd0a36c568a07383c54038b983'
password = "11cfdb7d49b9dea762dc0b02ec44fc5f65"#'hardik2021'
server = jenkins.Jenkins(host, username=username, password=password)

user = server.get_whoami()
version = server.get_version()
print(f"Hello {user['fullName']} jenkins version is {version}")
# job2_xml = open("job2.xml",mode='r', encoding='utf-8').read()
# server.create_job("job2",job2_xml)

# #view jobs
# jobs = server.get_jobs()
# print(jobs)

# #copy job
# server.copy_job('job2','job4')

# #update job
# updated_job_2 = open("job_2_updated.xml",mode='r',encoding='utf-8').read()
# server.reconfig_job('job2',updated_job_2)

# disable job
# server.disable_job('hello')

# build job
# server.build_job('job1')
# last_build_number = server.get_job_info('job2')['lastCompletedBuild']['number']
# for num in last_build_number:
#     print(num)
# print(last_build_number)

# # delete job
# server.delete_job('hello')

# # Craete_View
# view_config = open('sample_view.xml', mode='r', encoding='utf-8').read()
# server.create_view('job_List',view_config)

# # updated view
# updated_view_config = open('sample_view_updated.xml',mode='r',encoding='utf-8').read()
# server.reconfig_view("job_List",updated_view_config)

#delete view
server.delete_view('sample view')
