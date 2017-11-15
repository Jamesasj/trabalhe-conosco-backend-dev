#!/usr/bin/env python
# -*- coding: utf-8 -*-

from USUARIOWEB import app

if __name__=='__main__':    
    app.run('0.0.0.0',debug=True, port=80)