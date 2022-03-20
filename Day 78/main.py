
apiKey = ""


def main():
    global apiKey
    with open('api.json', 'r') as f:
        data = json.load(f)
        apiKey = data['api-key']


if __name__ == "__main__":
    main()
