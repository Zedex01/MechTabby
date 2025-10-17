import cv2, time, os
from pathlib import Path
import keyboard as kb
from util.ConCom import ConCom
'''
Outline 
    Fossil Hunter

    use keyboard module to take ss of game via obs

    inspect those based on 

'''
current_dir = current_dir = Path(__file__).parent.resolve()

def fossil_hunter():
    shiny = False
    counter = 0

    #Mount Controller port!
    #controller = ConCom('COM5')

    #Main Loop
    '''
    while not shiny:
        #Close Game
        controller.send("home")
        controller.send("x")
        controller.send("a")
        time.sleep(2)
        #relaunch game
        controller.send("a")
        controller.send("a")
        time.sleep(5)
        controller.send("a")
        
        #Talk to man
        for i in range(5):
            controller.send("a")

        #Check if shiny:
        kb.press('alt + k') #take ss
       ''' 
    #Grab Image:
    file_path = current_dir
    parent_dir = current_dir.parent
    target_path = parent_dir / "resources" / "Sample.jpeg"
    print(target_path)
    img = cv2.imread(target_path)
    if img is None:
        raise FileNotFoundError("Image not found or path is incorrect")


    # --- Step 2: Crop region of interest (x, y, width, height) ---
    x, y, w, h = 100, 100, 200, 200
    roi = image[y:y+h, x:x+w]
    
    # --- Step 3: Convert to HSV and create color mask (example: red) ---
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper bounds for red (two ranges for hue wraparound)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)
    
    # --- Step 4: Calculate red coverage percentage ---
    mask_pixels = cv2.countNonZero(mask)
    total_pixels = roi.shape[0] * roi.shape[1]
    color_percentage = (mask_pixels / total_pixels) * 100
    print(f"Red color coverage: {color_percentage:.2f}%")




def main():
    print("Starting...")
    fossil_hunter()


if __name__ == "__main__":
    main()