class ArtGallery:

    # STEP 1 - Parameterized Constructor
    def __init__(self, gallery_name, owner):
        self.gallery_name = gallery_name
        self.owner = owner
        self.artworks = []
        print(f"Art Gallery '{self.gallery_name}' owned by {self.owner} is ready!")

    # STEP 2 - Add an artwork
    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print(f"'{artwork}' added to the gallery.")

    # STEP 3 - Remove an artwork
    def remove_artwork(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print(f"'{artwork}' removed.")
        else:
            print(f"'{artwork}' not found in the gallery.")

    # STEP 4 - Display all artworks
    def display(self):
        print(f"\n--- {self.gallery_name} ---")
        print("Owner:", self.owner)

        if self.artworks:
            for i, artwork in enumerate(self.artworks, 1):
                print(f"{i}. {artwork}")
        else:
            print("No artworks yet. Add some!")

    # STEP 5 - Destructor
    def __del__(self):
        print(f"Art Gallery '{self.gallery_name}' has been closed. Goodbye!")


# Object Creation
my_gallery = ArtGallery("Creative Arts", "")

# STEP 6 - Menu-driven Program
while True:
    print("\n1. Add Artwork")
    print("2. Remove Artwork")
    print("3. View Gallery")
    print("4. Delete & Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        artwork = input("Enter artwork name: ")
        my_gallery.add_artwork(artwork)

    elif choice == "2":
        artwork = input("Enter artwork to remove: ")
        my_gallery.remove_artwork(artwork)

    elif choice == "3":
        my_gallery.display()

    elif choice == "4":
        del my_gallery
        break

    else:
       print("Invalid choice. Enter 1, 2, 3, or 4.")