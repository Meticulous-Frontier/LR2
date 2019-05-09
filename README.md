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

    1. Download a .zip file from the master branch or develop branch if you feel adventurous.
    2. Extract the contents of the .zip into the Lab Rats 2/game/ folder. (you should get a Mods folder in your game folder)
    3. Launch Lab Rats 2 and load up a save or start fresh.
	4. The main mods will be available in your bedroom right away (split between Mod Settings and Serum Mods).
    4. When adding ParadigmShift ModCore based Mods, skip time or play normally until the crisis event telling you about a computer in your bedroom is done.
    5. Go to the player's bedroom and use the PC via the "Do something..." menu.
    6. Hit the Mod Initialization button to initialize ParadigmShift mods and click through any messages.
    7. Done. 
	
All mods should now be available for the player, some add extra features, some add extra locations or extra actions while in a location.

You also get access to the Trollden CheatMod by pressing 'Z' in game.
