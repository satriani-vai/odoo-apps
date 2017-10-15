# -*- coding: utf-8 -*-
"""Return background image"""
from odoo.http import Controller, request, route
from werkzeug.utils import redirect


class DasboardBackground(Controller):
    """Dashboard background controller"""

    @route(['/background'], type='http', auth='user', website=False)
    def background(self, **post):
        """Redirects to the background image"""
        user = request.env.user
        company = user.company_id
        if company.background_allow_user and user.background_image:
            pass
        else:
            pass
