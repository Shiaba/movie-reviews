# Movie Reviews
![Am I responsive image of Number Guessing Game website]()

[You can view this site here]()


## Content


### [Features](#features-1)

- [Features yet to add](#features-yet-to-add)
- [Wireframes](#wireframes)

### [Database Design](#database-design-1)

### [Technologies Used](#technologies-used-1)

### [Testing](#testing-1)
  - [Manual testing](#manual-testing)
  - [Validator testing](#validator-testing)
  - [Accessibility](#accessibility)


### [Bug Encounters](#bug-encounters-1)
  - [Solved](#solved)
  - [Unsolved and scrapped features](#unsolved-and-scrapped-features)

### [Deployment](#deployment-1)


### [Credits](#credits-1)



## Features



### Features yet to add

- User can have the possibility to change password, delete their account or add image to profile.
- User can search for a specific movie name.

### Wireframes
I created the flowchart on [wireframe.cc](https://wireframe.cc/), then printed the creation instead of saving it.

- [Wireframe](/images/wireframe/main-page.png)
- [Wireframe](/images/wireframe/review-page.png)
- [Wireframe](/images/wireframe/sign-in.png)
- [Wireframe](/images/wireframe/sign-out.png)
- [Wireframe](/images/wireframe/sign-up.png)

[Back to top](#content)


## Database Design



## Technologies Used




### Libraries/Programs

- [Django 4.2.7](https://docs.djangoproject.com/en/4.2/releases/4.0/)
- [Django Allauth](https://docs.allauth.org/en/latest/)
- [Django Summernote](<https://summernote.org/>)
- [Django Crispy Forms](<https://django-crispy-forms.readthedocs.io/en/latest/#>)
- [Crispy Bootstrap 5](<https://pypi.org/project/crispy-bootstrap5/>)
- [Cloudinary](<https://cloudinary.com/>)
- [Psycopg2](<https://pypi.org/project/psycopg2/>)
- [Gunicorn](<https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/gunicorn/>)
- [Whitenoise](https://whitenoise.readthedocs.io/en/latest/)



## Testing




### Manual testing





### Validator testing



- [CI Python Linter]()
- [Python syntax checker]()

### Accessibility
 
 [Lighthouse testing]()


[Back to top](#content)

## Bug Encounters

### Solved

- I had issues with {% load static %} & loading in bootstrap & css. I solved it by installing whitenoise & add import path from urls.py.

### Unsolved and scrapped features:


[Back to top](#content)

## Deployment
- Create a new Heroku app
- Name app name & choose region
- Go to settings, add key = PORT, VALUE = 8000. Then add buildpacks(in this order):
  - heroku/python, 
  - heroku/nodejs

- On deployment method, github is chosen.
- Search repository name.

- Choose manual deploy & if wanted "Enable Automatic Deploys", which keeps the project up to date through your Github repository


[Back to top](#content)

## Credits

- I got my film favicon from: [Link here](https://icons8.com/icons/set/film)
- I got my secret key for env.py codes from: [Link here](https://randomkeygen.com/)
- I used bootstrap v.5.3 to build my pages: [Link here](https://getbootstrap.com/) 

### Code inspiration:

- In order to do things correctly, I've followed the "I Think Therefore I Blog" very carefully.
[Link here](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/)


[Back to top](#content)


