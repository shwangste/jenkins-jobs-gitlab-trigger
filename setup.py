from setuptools import setup

setup(
    name='jenkins-jobs-gitlab-trigger',
    version='0.1',
    description='Jenkins Job Builder Gitlab Trigger',
    url='https://github.com/shwangste/jenkins-jobs-gitlab-trigger',
    author='Wang Shouyu',
    author_email='shwangbupt@gmail.com',
    install_requires=[],
    entry_points={
        'jenkins_jobs.triggers': [
            'gitlab = jenkins_jobs_gitlab_trigger.gitlab:gitlab_triggers']},
    packages=['jenkins_jobs_gitlab_trigger'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])
