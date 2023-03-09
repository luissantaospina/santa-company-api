from flask import render_template


class Errors:

    @classmethod
    def page_not_found(cls, error):
        return render_template('404.html', error=error), 404

    @classmethod
    def method_not_allowed(cls, error):
        return render_template('405.html', error=error), 405

    @classmethod
    def server_error(cls, error):
        return render_template('500.html', error=error), 500
