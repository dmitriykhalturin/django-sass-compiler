[![PyPI](https://img.shields.io/pypi/v/django-sass-compiler)](https://pypi.org/project/django-sass-compiler/) 
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-sass-compiler)](https://pypi.org/project/django-sass-compiler/) 
[![PyPI - Django Version](https://img.shields.io/pypi/djversions/django-sass-compiler)](https://pypi.org/project/django-sass-compiler/) 
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/django-sass-compiler)](https://pypi.org/project/django-sass-compiler/) 
[![PyPI - Downloads](https://img.shields.io/pypi/dm/django-sass-compiler)](https://pypi.org/project/django-sass-compiler/) 

django-sass-compiler
===========

Simplify the use of [Sass](https://sass-lang.com/) in Django

Using `libsass`, compile all `.scss` files found in the paths defined in `settings.STATICFILES_FINDERS`

----------

Quickstart
------------

1.- It's available on [PyPI](https://pypi.org/project/django-sass-compiler/), so you can install it using `pip`

```
pip install django-sass-compiler
```

2.- Add `django_sass_compiler` to your `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...,
    'django_sass_compiler',
]
```

3.- Run `sass-compiler`

```
python manage.py sass-compiler
```
or combine with `runserver` command, useful with `--watch` argument. 
```
python manage.py runserver & python manage.py sass-compiler --watch
```

Arguments:
------------------
All arguments are optional and combinable

* `-s, --style` 

  Coding style of the compiled result. choose one of: `'nested'`, `'expanded'` (default), `'compact'`, `'compressed'`
 

* `-p, --precision` 

  Sets the number of digits of precision. 8 by default.
  
 * `-nb, --no-build` 
  
    Don't create `build` folder.
    
    ```
    app/
      |- static/
         |- app/
            |- scss/
               |- style.scss
            |- css/
               |- style.css
     ```
    
    instead
    
    ```
    app/
      |- static/
         |- app/
            |- scss/
               |- style.scss
            |- build/
               |- css/
                  |- style.css
    ```
    

* `-m, --map` 

   Build a source map.
   
* `-c, --clean`

  Remove old files before new compilation. 
  
  NOTE: This action will only take effect on current destination folder (`--no-build`).

* `-w, --watch` 

   Watch and compile files when `.scss` files are changed.
   
* `-i, --ignore` 

   Ignore files or directories matching this glob-style pattern. 
   Use multiple times to ignore more. 
   
   You can also define list paths to ignore in `settings.SASS_COMPILER_IGNORE_PATTERNS` environment variable.
   
   ```
   SASS_COMPILER_IGNORE_PATTERNS = [
      'app/scss/style.scss',
      'app/scss/test/*'
   ]
   ```
   
   NOTE: All patterns will applied in the path since the `static` folder to the file name. 
   
   Example: 
   
   To ignore `apps/app/static/app/scss/style.scss` the longest path would be:
   
   `python manage.py sass-compiler --ignore=app/scss/style.scss` or
   
   `python manage.py sass-compiler -i=**/**/style.scss` 
   
   or some other glob-style pattern.

@import
-------
To @import `.scss` files you must use absolute paths unless the files are at the same or less level, in that case you can use relative paths

```
some-app/
  |- static/
     |- some-app/
        |- scss/
            |- pages
                |- _timeline.scss
            |- _colors.scss
            |- style.scss
other-app/
  |- static/
     |- other-app/
        |- scss/
            |- _variables.scss
```

***some-app/style.scss***
```scss
@import 'other-app/scss/variables';
@import 'pages/timeline';
@import 'colors'
```

```scss
### WRONG ###
@import '../../variables'; 
```

Outputs
---------
##### Standard output:
```
$ python manage.py sass-compiler 
```
```
app/
  |- static/
     |- app/
        |- scss/
           |- _colors.scss
           |- style.scss
        |- build/
           |- css/
              |- style.css
```

##### With some argument output:

```
python manage.py sass-compiler --style=compressed --no-build --map
```

```
app/
  |- static/
     |- app/
        |- scss/
           |- _colors.scss
           |- style.scss
        |- css/
           |- style.min.css
           |- style.css.map
```
Licensing
---------

The project is licensed under the [BSD License](LICENSE).

