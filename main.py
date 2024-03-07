from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    # debug set as True, anytime the server would rerun anytime i make changes to the code.-> should be turned off during production


