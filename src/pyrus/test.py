from pyrus import str_manager as sm

german_titles = ["Die Kunst des Programmierens", 
                 "Ein Mann und sein Hund", 
                 "Über den Wolken", 
                 "Das ist der Hammer!", 
                 "Mit großer Macht kommt große Verantwortung", 
                 "Wenn du es wünschst", 
                 "in den Wäldern", 
                 "mit der Bahn", 
                 "ohne dich", 
                 "bei der Arbeit", 
                 "nach dem Regen"]

for title in german_titles:
    title_presenter = sm.TitlePresenter(title)
    print(title_presenter.present_title('de'))