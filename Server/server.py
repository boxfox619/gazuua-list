import unittest as ut

from app import app

if __name__ == '__main__':
    if app.config['TEST']:
        all_tests = ut.TestLoader().discover('tests', pattern='*.py')
        ut.TextTestRunner().run(all_tests)
    try:
        app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.debug, threaded=True)
    except KeyboardInterrupt:
        print('exit')
