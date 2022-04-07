from iching.api import AppFactory

app = AppFactory.create_app('dev')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)