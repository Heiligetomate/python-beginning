class chef:

    def make_chiken(self):
        print("The chef makes chiken.")
    def make_salad(self):
        print("The chef makes salad.")
    def make_special_dish(self):
        print("The chef makes special dish.")

class chinese_chef(chef):

    def make_fried_rice(self):
        print("The chef makes fried rice.")
    def make_special_dish(self):
        print("The chef makes cats.")


my_chef = chef()
my_chef.make_special_dish()

my_chinese_chef = chinese_chef()
my_chinese_chef.make_special_dish()