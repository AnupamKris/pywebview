"""Run Javascript code from Python."""

import webview
from webview.util import JavascriptException


def evaluate_js(window):
    result = window.evaluate_js(
        r"""
        var h1 = document.createElement('h1')
        var text = document.createTextNode('Hello pywebview')
        h1.appendChild(text)
        document.body.appendChild(h1)

        document.body.style.backgroundColor = '#212121'
        document.body.style.color = '#f2f2f2'

        // Return user agent
        'User agent:\n' + navigator.userAgent;
        """
    )

    print(result)

    try:
        result = window.evaluate_js('syntaxerror#$%#$')
    except JavascriptException as e:
        print(e)


if __name__ == '__main__':
    window = webview.create_window('Run custom JavaScript', html='<html><body></body></html>')
    webview.start(evaluate_js, window, debug=True)
