def for_loop():
    lang_list = ["Python’, ’JavaScript’, ’PHP’, ’Rust’, ’Solidity’, ‘Assembly"]
    count = 1
    for lang in lang_list:
        print("{}. {}".format(count,lang))
        count += 1
def my_msg(my_words):
    print("{}".format(my_words))
def main():
    run_loop = for_loop()
    while run_loop != "stop":
        run_loop = for_loop()
        my_msg("Begin Loop")
        my_msg("################ ")
        for_loop()
        my_msg("################ ")
        my_msg("End Loop ")
        run_loop = input("To end loop, type stop: ").lower().strip()
if __name__ == "__main__":
    main()
