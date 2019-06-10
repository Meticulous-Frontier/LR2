Collection of mods that are either entirely standalone or have a dependency on the Mod Core.

Folder structure is set up in a way that imitates a Class and its functionalities.

e.g the Room class contains both physical locations in the form of a room, but also actions via the "Do something..." menu.
Therefore the Room folder / directory houses both a room folder and an actions folder. 
This is to keep things sorted, but also due to neither of them being dependent on each other.
A room does not need an action and an action does not need a room to function, they can exist in codeform independently and be re- used where applicable.

Mechanics folder is where the framework of a mechanic will exist.
If possible, jam as many variable declerations and functions in a file there, so several files don't have to be looked through to see if a variable or function
serving a similar purpose already exist elsewhere.

If a RenPy screen is to be created e.g the Room Manager screen it should preferably be possible to call it without needing to have any prerequisites present.
I suggest having screens in their own .rpy file if you originaly indended to bundle in labels, actions, roles, rooms and such. In otherwords keep what content is added in addition
to the screen to a minimum.

How to Install:

    1. Download a .zip file from the master branch.
    2. Extract the Mods folder of the .zip into the <Lab Rats 2/game/> folder.
    3. You now should have a <Lab Rats 2/game/Mods> folder.
    3. Launch Lab Rats 2 and load up a save or start fresh.
    4. The MOD settings can be configured or en-/disabled from your bedroom.
    5. Done.

Unfortunatly the base game is not bug free. Check https://github.com/Tristimdorion/Lab-Rats-2/tree/bugfix for a repository that has updated versions of the game files, with fixes for all bugs people reported on the Patreon page.

