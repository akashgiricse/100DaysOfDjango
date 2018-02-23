# BlogApp

This is an online Blog site made using Django framework. 

### Current Features

* Post can have tags, posts can be retrieved from a perticular tag. 
* Post have markdown functionality, you can use markdonw while writing a post.
* You can also add a comment on a post.
* Posts can be shared via email.
* Site has RSS feeds functionality, you can subscribe to RSS feeds.
* There is a separate list of latest posts and most commented posts. 


### Getting started with development
Dependenciies:
- Python 3.6.x
- Django 1.11.x
- MySQL 5.7.x
- Ubuntu 17.04 or later

#### 1. Clone this repoistory
```bash
git clone https://github.com/akashgiricse/100DaysOfDjango.git
cd BlogApp
```

#### 2. Install the [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)
Follow [instructions on official documentation page](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

#### 3. Create the virtualenv
```bash
## run following command from `BlogApp/mysite` directory
mkvirtualenv blog_app -a "$(pwd)" -p python3.6
```

#### 4. Install python packages
```bash
## Activate the virtualenv which you created on the last step
workon blog_app
pip install -r requirements.txt
```

#### 5. Setup the database
*TODO - Add instructions for this when we start using MySQL database.*

#### 6. Run database migrations
```bash
python manage.py migrate
```


#### 7. Run development server
```bash
python manage.py runserver
```


### Contribute
----------
- Issue Tracker: [Issues](https://github.com/akashgiricse/100DaysOfDjango/issues)
- Source Code: [Here](https://github.com/akashgiricse/100DaysOfDjango/tree/master/BlogApp)

### Contributors
----------

* [Akash Giri](https://github.com/akashgiricse)

### Support
----------
* If you are having issues, please let me know.<br>
  You can send a mail at buggyrango@gmail.com

### Screenshots 
---------
**[here](https://github.com/akashgiricse/100DaysOfDjango#1-blog-app)**

### License
----------
MIT License

Copyright (c) 2018 Akash Giri

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.