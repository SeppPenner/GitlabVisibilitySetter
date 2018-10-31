GitlabVisibilitySetter
====================================

GitlabVisibilitySetter is a script to make all repositories on Gitlab publicly accessible. (Useful for all that are [#movingtogitlab](https://twitter.com/hashtag/movingtogitlab?lang=en))
The script was written and tested in Python 3.7.1.

[![Build status](https://ci.appveyor.com/api/projects/status/mc210w5866dgt9wi?svg=true)](https://ci.appveyor.com/project/SeppPenner/gitlabvisibilitysetter)
[![GitHub issues](https://img.shields.io/github/issues/SeppPenner/GitlabVisibilitySetter.svg)](https://github.com/SeppPenner/GitlabVisibilitySetter/issues)
[![GitHub forks](https://img.shields.io/github/forks/SeppPenner/GitlabVisibilitySetter.svg)](https://github.com/SeppPenner/GitlabVisibilitySetter/network)
[![GitHub stars](https://img.shields.io/github/stars/SeppPenner/GitlabVisibilitySetter.svg)](https://github.com/SeppPenner/GitlabVisibilitySetter/stargazers)
[![GitHub license](https://img.shields.io/badge/license-AGPL-blue.svg)](https://raw.githubusercontent.com/SeppPenner/GitlabVisibilitySetter/master/License.txt)

# Steps to use this script:
1. Migrate your projects from github to gitlab: https://docs.gitlab.com/ee/user/project/import/github.html
2. Wait until finished
3. Generate a personal access token on gitlab: https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html
4. Fill in your user name and the generated access token in the following lines in the
[GitlabVisibilitySetter.py](https://github.com/SeppPenner/GitlabVisibilitySetter/blob/master/GitlabVisibilitySetter.py) file:
```python
userName = "YourUserName"
token = "1234567890"
```

5. Install all required pip package dependencies with:
```python
pip install -r requirements.txt
```

6. Run the project using:
```bash
python GitlabVisibilitySetter.py
```

# For more information see:
https://docs.gitlab.com/ee/api/#authentication

https://docs.gitlab.com/ee/api/projects.html#list-user-projects

https://stackoverflow.com/questions/50763143/when-movingtogitlab-is-there-a-possibility-to-set-all-imported-projects-to-pub

Change history
--------------

* **Version 1.0.0.0 (2018-06-09)** : 1.0 release.