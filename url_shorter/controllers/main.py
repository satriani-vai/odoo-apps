# -*- coding: utf-8 -*-
from werkzeug.exceptions import NotFound
from werkzeug.utils import redirect

from odoo import http


class UrlShorterController(http.Controller):
    
    @http.route('/s/<string:token>', type='http', auth='public')
    def shorter(sefl, token, **kw):
        UrlShort = http.request.env['url.shorter']
        short = UrlShort.search([('token', '=', token), ('active', '=', True)], limit=1)
        if short:
            short.write({
                'redirect_number': short.redirect_number + 1
                })
            return redirect(short.long_url)
        else:
            raise NotFound()
