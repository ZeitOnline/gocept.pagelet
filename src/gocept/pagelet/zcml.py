# Copyright (c) 2007 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id$

import zope.configuration.fields
import zope.interface
import zope.publisher.interfaces.browser
import zope.viewlet.metaconfigure

import z3c.pagelet.zcml
import z3c.template.zcml

import gocept.pagelet.viewletpage


class IPageletDirective(z3c.pagelet.zcml.IPageletDirective):
    """A directive to easiliy register a new pagelet with a layout tempalte.

    """

    class_ = zope.configuration.fields.GlobalObject(
        title=u"Class",
        description=u"A class that provides attributes used by the pagelet.",
        required=False,
        )

    template = zope.configuration.fields.Path(
        title=u'Layout template.',
        description=u"Refers to a file containing a page template (should "
                     "end in extension ``.pt`` or ``.html``).",
        required=False,
        )


def pageletDirective(
    _context, name, permission, class_=None, for_=zope.interface.Interface,
    layer=zope.publisher.interfaces.browser.IDefaultBrowserLayer,
    allowed_interface=None, allowed_attributes=None, template=None,
    **kwargs):

    if class_:
        new_class = class_
    else:
        new_class = type('SimplePagelet', (object, ), {})

    z3c.pagelet.zcml.pageletDirective(
        _context, new_class, name, permission, for_, layer,
        allowed_interface, allowed_attributes)

    if template:
        z3c.template.zcml.templateDirective(
            _context, template, for_=new_class, layer=layer)


class ViewletPageDirective(object):

    def __init__(self, _context, name, permission,
                 class_=gocept.pagelet.viewletpage.ViewletPage,
                 **kwargs):
        self._context = _context
        self.name = name
        self.permission = permission
        self.class_ = class_
        self.kwargs = kwargs

    def __call__(self):
        z3c.pagelet.zcml.pageletDirective(
            self._context, self.class_, self.name, self.permission,
            **self.kwargs)

    def viewlet(self, _context, name, permission, layer=None, **kwargs):
        kwargs["manager"] = gocept.pagelet.viewletpage.IViewletPageManager
        zope.viewlet.metaconfigure.viewletDirective(
            _context, name, permission,
            layer=layer or self.kwargs.get("layer"),
            **kwargs)
