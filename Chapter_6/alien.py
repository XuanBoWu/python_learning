alien_0 = {'color': 'green', 'point': 5}

print(alien_0)
print(alien_0['color'])
print(alien_0['point'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)


## Change alien color to yellow.

alien_0['color'] = 'yellow'

print(f"The alien color is now {alien_0['color']}")

## 设置外星人速度为 ‘中等’
alien_0['speed'] = 'medium'
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人速度肯定很快
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"Now position: {alien_0['x_position']}")

del alien_0['color']
print(alien_0)


