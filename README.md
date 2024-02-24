# Overview

This script was created to repeat a quest in Granblue Fantasy Relink as long as you want. The game window needs to be active for this to work. The newest piece of this script also added link time interaction and revives.

## Instructions:
Once you start a quest, start the script, and make sure the game window is active. That's it.

If your game is in another language other than English then you'll need to provide new images for the code to look for.

## Troubleshooting:
If you find that the repeat quest functionality isn't working there are a few things to try:
1. Ensure the game window is active after starting the script.
2. Monitor resolution can impact if the code finds the images or not, so you can retake the photos and put them into the images folder (rename them to match the current name).
3. You could also lower the confidence values for the locateOnScreen for whichever image doesn't appear to be working appropriately. For example, if the quest won't complete you can stop the script, change the confidence value from 0.9 to 0.8 and retry it.
