import json


def main():
    close_script = False
    while not close_script:
        print('Select an option:\n'
              '1. Load a JSON file\n'
              '2. Create a new JSON file\n'
              '3. Exit')
        selection = int(input())
        if selection == 1:
            print('Input path to the target JSON file')
            file_path = input()
            with open(file_path) as input_file:
                data = json.load(input_file)
                for dci in data:
                    print('DCI: {}, Name: {}, TotalPoints: {}'.format(dci,
                                                                      data[dci]['name'],
                                                                      data[dci]['total_points']))
        elif selection == 2:
            print('File name:')
            file_path = input()
            json_dict = {}
            print('Type "exit" to close the writing loop (checked after each player)\n'
                  'Type "next_round" to continue to the next round')
            write_n_close = False
            n_round = 1
            while not write_n_close:
                print('Round" {}\nDCI: '.format(n_round))
                dci = input()
                if dci == 'exit':
                    write_n_close = True
                    with open(file_path, 'w') as file:
                        json.dump(json_dict, file)
                    break
                elif dci == 'next_round':
                    n_round += 1
                    print('Round" {}\nDCI: '.format(n_round))
                    dci = input()
                if dci not in json_dict:
                    json_dict[dci] = {}
                if 'name' not in json_dict[dci]:
                    print('Player Name: ')
                    name = input()
                    json_dict[dci]['name'] = name
                print('Points for Round #{}: '.format(n_round))
                points = int(input())
                json_dict[dci][n_round] = {}
                json_dict[dci][n_round]['points'] = points
                if 'total_points' not in json_dict[dci]:
                    json_dict[dci]['total_points'] = points
                else:
                    json_dict[dci]['total_points'] += points
        elif selection == 3:
            close_script = True
        else:
            print('Chose an option from 1 to 3')


if __name__ == "__main__":
    main()

