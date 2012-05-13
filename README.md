Party game is a seekrit open-source project. It's totally not about party games on the internet, at all. Nope. Nothing to do with that. Nothing at all.

It also totally isn't using similar internals to SMOKE, such as Python 2.7, SQLite, and Flask.

Usage
=====

1. Create a config.py file - see config.py.example
2. Open the Python REPL and `import partygame.db`, then run `partygame.db.init_db()`
3. For development, just run `runserver.py`. For production, set up your web server with WSGI and make sure `/static` is redirected to the `static` folder.
4. Register an account
5. Again using the interface of your choice, set the user you just created's admin value to `1`
6. Done!

License
=======

    Copyright (c) 2012 Andrew Faulds

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
