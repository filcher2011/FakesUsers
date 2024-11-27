#FakesUsers 3.7 from filcher2011
from random import choice, randint

class Fu:
    def __init__(self, region: str) -> str:
        self.name = "FakesUsers"
        self.version = "3.7"
        self.patch = "2024.03.11R"

        if region == "":
            self.reg = "ru"
        else:
            self.reg = region

        self.name_m_ru = ['Андрей','Афанасий','Абдул','Антон','Архип','Анатолий','Александр','Алексей','Альберт','Аксен',
                        'Богдан','Борис','Бронислав','Буклаг',
                        'Вадим','Владислав','Виктор','Валерий','Валентин','Василий','Виталий','Всеволод',
                        'Давид','Давыд','Даниель','Данил','Даниил','Дмитрий','Доброслав',
                        'Евгений','Евсений','Ефрем','Епифан','Егор',
                        'Жан',
                        'Завид','Захар',
                        'Иван','Игнат','Игорь','Иосиф','Изяслав','Илья','Ильнар',
                        'Кирилл','Казимир','Кузьма',
                        'Ладислав',
                        'Мазай','Макар','Максим','Марат', 'Мурат', 'Матвей','Марк', 'Мирослав',
                        'Никита','Нифёд','Николай','Назар',
                        'Олимп','Олег',
                        'Павел','Пётр',
                        'Роман','Родим','Радислав','Руслан','Рюрик',
                        'Савелий','Савва','Семён','Станислав','Спартак',
                        'Фёдор','Филипп','Федот',
                        'Эдвард','Эльдар','Эдгар','Эрик',
                        'Юрий','Юлий',
                        'Якив','Яков','Ян','Ярополк','Ярослав',]
        
        self.name_m_en = ['Aaron','Abraham','Adam','Adrian','Aidan','Alan','Albert','Alejandro','Alex','Alexander','Alfred','Angel','Anthony','Austin',
                          'Benjamin','Bernard','Blake','Brandon','Brian','Bruce','Bryan',
                          'Carl','Christopher','Christian','Cody','Connor',
                          'Daniel','Diego','Devin','Dennis',
                          'Edward','Ethan','Evan','Eric'
                          'Francis','Fred',
                          'Gabriel','Gavin','George','Gilbert','Gerld',
                          'Harry','Harold','Henry','Hunter','Howard',
                          'Ian','Isaac','Isaiah',
                          'Jack','Jackson','Jacob','Jason','Jake','Jordan','Jonathan','John','Justin','Joseph',
                          'Kevin','Kyle',
                          'Lucas','Louis','Logan','Lewis',
                          'Martin','Mason','Michael','Morgan',
                          'Norman','Neil','Nathaniel','Nathan',
                          'Oscar','Oliver','Owen',
                          'Patrick','Peter','Philip',
                          'Ralph','Raymond','Reginald','Richard','Robert','Ryan','Ronald',
                          'Samuel','Stanley','Steven','Seth','Sebastian',
                          'Thomas','Timothy','Tyler',
                          'Wallace','Walter','William','Wyatt',
                          'Xavier',
                          'Zachary',]
        
        self.name_m_de = ['Achim','Adelbert','Adolf','Alban','Arne','Amand','Alwin','Aurel','August','Alois','Anselm',
                          'Baldur','Baptist','Bartholomäus','Beat','Bruno','Bonifaz',
                          'Carl','Carsten','Cord','Claus','Conrad',
                          'Detlef','Didi','Dirk','Dietrich','Dietmar',
                          'Ebbe','Emil','Eckhart','Engel','Erhard','Engelbert',
                          'Ferdi','Fester','Friedemann','Frej',
                          'Gabi','Georg','Gereon','Gero','Gert','Gottlieb','Günther',
                          'Hagan','Hannes','Heinrich','Heiko','Hermenegild',
                          'Ignatz','Immanuel','Ingo','Ingolf','Ivo',
                          'Jochem','Jochen','Jochim','Johann','Jörg','Jürgen',
                          'Karlmann','Kasimir','Körbl','Kurt',
                          'Lammert','Lanzo','Lorenz','Ludwig','Lutz','Lukas',
                          'Manfried','Marwin','Meinard','Mose','Moritz','Matthäus',
                          'Nickolaus','Niklaus',
                          'Ortwin','Othmar','Otto','Ottokar','Ottomar',
                          'Pankraz','Parsifal','Philipp','Poldi',
                          'Raffael','Reimund','Reiner','Rambert','Reimund','Rein',
                          'Sascha','Siegfried','Siegward',
                          'Theophil','Till','Tillo','Torben','Traugott',
                          'Udo','Urs','Utz','Uwe',
                          'Veit','Vester','Vinzent','Vinzenz','Volker',
                          'Walther','Wenzeslaus','Willi','Werther','Wulf',
                          'Xaver',]
        
        self.surname_m_ru = ['Аношкин','Апатов','Апятов','Александров','Авлипов','Анатошкин','Аримченко','Абаранов','Адамов','Авличекко',
                        'Бытряков','Битряков','Борисов','Балипин','Базякин','Бурятов','Батурин',
                        'Ветров','Ветряков','Вадмиран','Вичатов','Викрович','Взаров','Версталин','Вокупин',
                        'Демитров','Донской','Денистарин','Дуров','Дамиченко','Доброградов','Далинин',
                        'Ермаков','Ефмеич','Егоров','Екатин',
                        'Жаровцев','Жирин','Жостченко','Жипин','Жилин',
                        'Задоров','Затриков','Зосин','Зазарин','Захаров','Захаев',
                        'Ильбанов','Инитаров','Известин','Итмирин','Изаченко','Избанов','Иоритов',
                        'Кристалин','Крост','Кисмисов',
                        'Лебедев','Литартасов','Ликрасов','Лесуч','Лобиченко',
                        'Митин','Матросов','Миклин','Меривич', 'Муратов', 'Матвеев','Мустин','Маслеников',
                        'Надурин','Нифёдов','Назаров','Николаев',
                        'Останткин','Остмов',
                        'Петроградов','Подушкин','Пирин','Пиров',
                        'Рокосовский','Радимов','Рютриков','Русланов','Ралин',
                        'Сантропов','Семёнов','Семечкин','Стасин','Спартаков',
                        'Фёдоров','Филиморов','Филатов',
                        'Хитров','Хитбаров','Хабарин',
                        'Шевцов','Шитрин','Шитин',
                        'Эдринский','Эшинский','Эпченко','Эрикс',
                        'Ютропов','Юлиев',
                        'Ярков','Яковлев','Ялубин','Явилин','Яшин',]
        
        self.surname_m_en = ['Akins','Alameda','Absher','Abramson','Alexandre','Alldredge','Alvarado','Amado',
                             'Barksdale','Barnard','Barney','Barrientos','Bartholomew','Bateman','Beckmann','Behm',
                             'Caballero','Caban','Canizales','Caplinger','Cardwell','Carleton','Cashman','Caudle',
                             'Daw',]
        
        self.surname_mf_de = ['Abegg','Abend','Ada','Adelung','Aichinger','Adolph','Adolphus','Ahlmann','Ahrens',
                             'Baal','Baatz','Bachmann','Bachus','Backstedt','Baeker','Bahlo','Baigelman','Baldwin',
                             'Cananis','Cimmerman','Clowes','Claus','Cram','Crap',
                             'Dahl','Daschke','Dangel','Deissler','Dempewolf','Delitzsch','Delbruck','Dasler','Danneberg',
                             'Eberl','Ebert','Egner','Edward',
                             'Fahrenheit','Fagg','Fassler','Fehr','Fauner',
                             'Gabler','Gardner','Gastenveld','Gaubatz','Geisel',
                             'Haberfeld','Hache','Haecke','Haff',
                             'Idesheim','Isekenmeir','Inken','Ingram',
                             'Jachman','Jauch','Jhering','Jotten','Jost',]
        
        self.name_f_ru = [ 'Аглая','Арина','Арина','Анна','Августина','Аделина','Ангелина','Анжела','Анфиса','Ася', 'Анастасия', 'Александра',
                        'Валентина','Владислава','Ваннеса','Виктория','Вероника','Вера',
                        'Галина',
                        'Дария','Диана','Дора',
                        'Елена','Евгения','Ева','Екатерина','Елизавета',
                        'Жанна',
                        'Зарина','Зоя',
                        'Инна','Ива','Ирина',
                        'Калина','Кира', 'Кристина',
                        'Лариса','Любовь','Лина',
                        'Майя','Марина','Мария','Марьяна',
                        'Ника','Надежда',
                        'Олеся','Оксана','Ольга',
                        'Полина',
                        'Рая','Раиса','Роза','Рита',
                        'Сабина','София','Стефания',
                        'Таисия','Татьяна',
                        'Эля','Эльга',
                        'Яна','Ярина',]
        
        self.name_f_en = ['Ann','Adelina','Amelia','Avery','Ada',
                          'Bailey','Barbara',
                          'Chloe','Cecilia','Catherine',
                          'Daisy','Danielle','Delia','Dorothy',
                          'Elizabeth','Ella','Erin',
                          'Freda','Fiona','Faith',
                          'Gloria','Grace',
                          'Helen','Hannah','Haley','Hailey',
                          'Isabel','Isabella',
                          'Jane','Jada','Julia','Joyce',
                          'Katherine','Kayla','Kylie','Katelyn','Kaitlyn',
                          'Lucy','Luccile','Lorna','Lily','Leslie','Lillian',
                          'Maria','Madeline','Mabel','Monica','Molly','Michelle','Mia',
                          'Nancy','Natalie','Nora',
                          'Olivia',
                          'Priscilla','Penelope','Pauline','Pamela',
                          'Rita','Riley','Rachel','Rose',
                          'Sandra','Sara','Sylvia','Shirley',
                          'Trinity','Vanessa','Victoria','Violet','Virginia',
                          'Winifred',
                          'Yvonne',
                          'Zoe',]
        
        self.name_f_de = ['Adele','Adelheid','Annegret','Augusta','Annemarie','Annegret','Amelie','Anina','Anke','Aleida','Aleit',
                          'Beate','Berta','Bertha','Bettina','Brigitta','Brigitte','Brunhild','Brunhilde',
                          'Cäcilia','Cäcilie','Caecilia','Carolin','Cordula',
                          'Daniela','Dietlinde','Dorothea','Dörthe',
                          'Erna','Elma','Elise','Elke','Elli','Ebba',
                          'Felicie','Felicitas','Felizitas','Fränze','Friede','Fritzi',
                          'Gabi','Gabriele','Gerda','Gerhild','Gerlinde','Gisa','Gundula',
                          'Hanna','Heilwig','Heinrike','Henriette','Hermine','Hildegard',
                          'Ilsa','Ilse','Irmingard','Ivonne',
                          'Jasmin','Jessika','Johanna','Josefine','Josepha','Juliana','Justine','Jutta','Jutte',
                          'Karla','Katharina','Katarine','Katja','Katrin',
                          'Lea','Lene','Liesl','Lilo','Lulu','Lutgard',
                          'Maja','Margarete','Marlis','Mitzi','Minna',
                          'Nadja','Nathalie','Nele','Nicola',
                          'Oda','Ottilie',
                          'Paula','Pauline','Petronella',
                          'Raffaela','Raimunde','Reinhilde','Roswitha',
                          'Susi','Swanhild','Swanhilda','Sybille',
                          'Tabea','Tanja','Tatjana','Thea','Theda','Thekla',
                          'Ute','Uschi','Ulrike','Ursel',
                          'Valeska','Verena','Vreni',
                          'Wibke','Wilhelmina','Wilma',
                          'Zella','Zenzi','Zilla','Ziska',]
        
        self.surname_f_ru = ['Алианна','Альяна','Атрасова','Апяткова','Авиолова','Анатошкина','Адианова','Асокина','Асотина','Алимарова',
                        'Бистибюлина','Бистинова','Бильбина','Балина','Базякина','Бурова','Батросова',
                        'Виталина','Верченко','Вистибюлина','Волчанова','Васюткина','Взирова','Ветрова','Вилина',
                        'Добровая','Дианнова','Деченко','Дякина','Дасимова','Добрич','Долинина',
                        'Етиспатова','Еровенич','Есушкина','Едурина',
                        'Жилинна','Жигулич','Житрипевич','Жигина','Жорина',
                        'Зимаидова','Зимина','Зосина','Зарецская','Замитрова','Зюсина',
                        'Ильнасова','Ирибинко','Истучева','Исшенко','Ипритова','Илизова','Иоритова',
                        'Кристальная','Кристинова','Космович',
                        'Ликрасова','Литрасова','Лобина','Логина','Лосинова',
                        'Миликанова','Мутулина','Марошина','Мертеич', 'Муратова', 'Матвеева','Мулина','Мастович',
                        'Никитова','Неримова','Настюшина','Николаева',
                        'Осенняя','Отмирова',
                        'Петрокамчатская','Полинина','Пирова','Пасутина',
                        'Роловинина','Ракусина','Рюрович','Руслаченко','Ралина','Родова',
                        'Сандалина','Семикрасова','Сачкова','Салтыкова','Спорина',
                        'Фёдорова','Филиморова','Филатова',
                        'Хирипова','Хиширина','Хочубина',
                        'Шевцова','Шитина','Шитрина',
                        'Эдолинова','Эльдарова','Эпченко','Эпистатова',
                        'Ютропова','Юлиева',
                        'Яркова','Яковлева','Ялубина','Явилина','Яшина',]
        
        self.surname_f_en = ['Butler','Bishop','Blare','Bladshaw','Brooks','Bush','Babcook',
                             'Gray',
                             'Red',]
        
        self.num_part1_ru = ['001','002','003','004','005','006','007','008','009',]

        self.num_part2_ru = ['2415537','4636643','6438943','0077543','6536673','3564575','3513355','0006559',
                       '9997590','8654581','1010853','6695888','4256343','6476754','1215467','53674367',]
        
        self.email = ['rei793h','AlexHyIO','PORAMT1K','lsui1994','4345g2aw24y',
                      'georagl:wedmak','neomeo228','fifynya','930ip42','4444ererer4444',
                      'uow54io','xxxkeepmedownxxx','tytyr1n3','fil4rok','0101hh0101','QQooyyuurrnnIIwwqqxxzzQQ','popyt1k','tyrn1k','776',
                      'heroesRusich2007','igrikoh93w','3232lisabonka3232','youtubeTheBest','goverment_the_RCX','le4ko',
                      'tribasyakin_nikoplay','godEX55','beebag','3432','botik_shotik','joj1sus','LXCVWERSI',
                      'boris_ermakov75','barbara33','poplin_goblin','leeasaANDvanesa','so2H2O',
                      'yorik1900','kidsfam78','jackPreston89','l0lGRENDY']
        
        self.login = ['georg','dotatop','fakerCCX','marii67','CMEPTb_B_KYCTAX','Pavlik9090','Zs1mpleV','TOPOLb_NA_OPYCKE','poritta','usoup53',
                      'likras','dorim_sakatov1989','kit0w0','7Andrew7UwU7Kirillov7','JacksonBest','Marin1A2A3A4','1tvista','4636745','rirorira','Zhushik1',
                      'SlengTab','Peorvits','jErR','NeoNexus','Ghost0x0x0Bust','joustin_eekn','KISSunya','tyrnado','youIbest','GerBeast',]
        
        self.email_index = ['@example.ru','@outlook.qq','@mcrs.com','@python-test.pyt', '@zimzas.yan']

        self.faddres_ru = ['Грибоедова','Ленина','Жаргонская','Сосоновая','Еловая',
                  'Пугачева','Комунистическая','Социалистическая','Дектярёва','Гагарина',
                  'Черная','Победителей','Мира','Малеева','Захарова', '20 октября']
        
        self.faddres_en = ['Green','Black','White','Red','Yellow','Purple','World War II','Heroes',
                           'Washincton','San-Alnaser','Uping','Down','Up','Technologys','Jackson','Security',
                           'Gloria','the 25th December','Carib','West','Douglas MacArthur','Violet','Labor','World',]
        
        self.faddres_de = ['Buelowstrasse','Hans-Grade-Allee','Kastanienallee','Motzstr','Lützowplatz','Gotzkowskystraße','Messedamm',
                           'Koenigstrasse','Bissingzeile','Rohrdamm','Rudolstaedter Strasse','Kantstrasse','Ellmenreichstrasse','Alt-Moabit',
                           'Lange Strasse','Waldowstr','Hollander Strasse','Lietzenburger Straße','Pohlstrasse','Park Str.','An der Alster',
                           'Grolmanstraße','Spresstrasse','Sonnenallee','Stresemann str.','Eichendorff str.','Rohrdamm','Güntzelstrasse',]
        
        self.fpassword = ['gpt4','aio','fake','ny_3#','reews','saVva_g0v0n','lilis','JACK','Kirill',
                          'qwerty123','bhor','1234567890abcdifg0987654321','3244310084y4','##836/@tg__inkt/**r','3t77++wwu%#!gj,_h',
                          'hhjj__++__%$43','35FFFFFPRES#4_+@$(!)','343494602UIUIH&*#__#(^&#___^#3663)256huh3',
                          '23425633','4625267','462646andrew','3678965','9686784','347264623jonh','3537767','2326567548','1234567876543292356loop',
                          '3235235','25246','6346437','5685856','23432325','5857978','098-89090','67336576','76354733',]
        
        self.fcity_ru = ['Санкт-Петербург','Москва','Великий Новгород','Тверь','Рязань','Ростов-на-дону','Владимир',
                         'Иваново','Ковров','Гусь-Хрустальный','Кострома','Плёс','Сочи','Казань','Иннополис',
                         'Ульяновск','Уфа','Шуя','Нижний Новгород','Екатеринбург','Челябинск','Омск','Краснодар',
                         'Красноярск','Томск','Новосибирск','Братск','Хабаровск','Владивосток','Южный Сахалин','Иркутск',]
        
        self.fcity_en = ['Washington','New-Your','Las-Vegas','Los-Sangeles','San-Francisco','Dallas','San-Diego','Miami','Chicago','Columbus',
                         'Portland','Phoenix','Denver','San-Antonio','Houston','Atlanta','Charlotte','Detroit','Seattle','Boston','Scottsdale',]
        
        self.fcity_de = ['Berlin','Hamburg','Kiel','Hannover','Bremen','Postdam','Mainz','Stuttgart',]
        
        self.fname_link = ['iresko','egebody_entername','trololoshkin','mirrorandmirror','loopi_robot','jeuisu_ponoramic','heard_reatom','jecksy',
                           'kitstant','minesheredan','ghpr','bleensy','oppling','phonemaster','kkp','qwerty_comt',
                           'justin_eredanchi','macfontestrenc','goologren','yayoshi','dinamic_irland','returnboyses','syspoco','iydarn',]
        
        self.findex_link = ['su','ru','org','net','com','ai','de',]

        self.frus_num = ['A','E','T','O','P','H','K','X','C','B','M',]

        self.fde_num = ['B','L','H','T','A','D','M','X','R','A',]

        self.fde_num_index = ['A','AA','AB','ABG','AS','B','BA','BAD','BAR','BB','BOR',
                              'C','CE','CB','D','DEG','DD','DH','ED','EE','EF','ES',]

        self.fpartone_text_ru = ['Я','Ты','Кто-то']
        
        self.fparttwo_text_ru = ['пошел','ушел']

        self.fpartthree_text_ru = ['есть в фастфуд','в дом','в гости','за хлебом','в отпуск','на работу','в магазин','в бар',]

        self.fpartone_text_en = ['I', 'You', 'Someone',]

        self.fparttwo_text_en = ['went', 'gone',]

        self.fpartthree_text_en = ['eat at fast food','to the house','on a visit','for bread','on vacation','to work','to the store','to the bar',]

        self.fpartone_text_de = ['Ich','Du','Jemand',]

        self.fparttwo_text_de = ['ging','gegangen',]

        self.fpartthree_text_de = ['bei Fast Food essen','zum Haus','bei einem Besuch','für Brot','im Urlaub','arbeiten','zum Geschäft','zu der Bar',]

        self.fjob_ru = ['Офицер Полиции','Пожарный','Менеджер','Продавец','Врач','Хирург','Механик','Таксист',
                        'Пилот','Военный','Адвокат','Судья','Редактор СМИ','Учитель','Строитель','Священик',]

        self.fjob_en = ['Police Officer','Fireman','Manager','Salesman','Doctor','Surgeon','Mechanic','Taxi driver',
                        'Pilot','Military','Advocate','Judge','Media Editor','Teacher','Builder','Priest',]
        
        self.fjob_de = ['Polizist','Feuerwehrmann','Manager','Verkäufer','Arzt','Der Chirurg','Mechaniker','Taxifahrer',
                        'Pilot','Militär','Fürsprecher','Richter','Medienredakteur','Lehrer','Baumeister','Priester',]
    
    def info(self):
        #This function displays information about the module, its name, version and patch

        return(f'Python library {self.name}, version {self.version}, patch {self.patch}')

    def fake_name(self, gender: str) -> str:
        self.gen = gender
        gn = self.reg
        if gn == 'ru':
            if self.gen == 'male':
                return(f'{choice(self.name_m_ru)} {choice(self.surname_m_ru)}')
                
            elif self.gen == 'female':
                return(f'{choice(self.name_f_ru)} {choice(self.surname_f_ru)}')
            
            else:
                return('Error №1! Enter True Value!')

        elif gn == 'en':
            if self.gen == 'male':
                return(f'{choice(self.name_m_en)} {choice(self.surname_m_en)}')
            elif self.gen == 'female':
                return(f'{choice(self.name_f_en)} {choice(self.surname_f_en)}')
            else:
                return('Error №1! Enter True Value!')
            
        elif gn == 'de':
            if self.gen == 'male':
                return(f'{choice(self.name_m_de)} {choice(self.surname_mf_de)}')
            elif self.gen == 'female':
                return(f'{choice(self.name_f_de)} {choice(self.surname_mf_de)}')
            else:
                return('Error №1! Enter True Value!')
            
        else:
            return('Error №2! Unknow region!')
            
    def fake_lastname(self, gender: str) -> str:
        self.gen = gender
        gn = self.reg
        if gn == 'ru':
            if self.gen == 'male':
                return(f'{choice(self.surname_m_ru)}')
            elif self.gen == 'female':
                return(f'{choice(self.surname_f_ru)}')
            else:
                return('Error №1! Enter True Value!')
            
        elif gn == 'en':
            if self.gen == 'male':
                return(f'{choice(self.surname_m_en)}')
            elif self.gen == 'female':
                return(f'{choice(self.surname_f_en)}')
            else:
                return('Error №1! Enter True Value!')
            
        elif gn == 'de':
            if self.gen == 'male':
                return(f'{choice(self.surname_mf_de)}')
            elif self.gen == 'female':
                return(f'{choice(self.surname_mf_de)}')
            else:
                return('Error №1! Enter True Value!')
        
        else:
            return('Error №2! Unknow region!')

    def fake_number(self):
        gn = self.reg
        if gn == 'ru':
            return(f'+7{choice(self.num_part1_ru)}{choice(self.num_part2_ru)}')
        elif gn == 'en':
            return(f'+1{choice(self.num_part1_ru)}{choice(self.num_part2_ru)}')
        elif gn == 'de':
            return(f'+49{randint(100, 999)}{randint(1000000, 9999999)}')
        
        else:
            return('Error №2! Unknow region!')
    
    def fake_addres(self, full: bool) -> str:
        f = False
        self.f = full
        gn = self.reg
        if gn == 'ru':
            if self.f == False:
                return(f'ул. {choice(self.faddres_ru)} {randint(1, 120)}')
            elif self.f == True:
                return(f'г.{choice(self.fcity_ru)}, ул. {choice(self.faddres_ru)} {randint(1, 120)}')
            elif self.f == '':
                return(f'ул. {choice(self.faddres_ru)} {randint(1, 120)}')
            
        elif gn == 'en':
            if self.f == False:
                return(f'{randint(1, 120)} {choice(self.faddres_en)} Streed')
            elif self.f == True:
                return(f'{choice(self.fcity_en)} City, {randint(1, 120)} {choice(self.faddres_en)} Streed')
            elif self.f == '':
                return(f'{randint(1, 120)} {choice(self.faddres_en)} Streed')
            
        elif gn == 'de':
            if self.f == False:
                return(f'{choice(self.faddres_de)} {randint(1, 100)}')
            elif self.f == True:
                return(f'{choice(self.fcity_de)}, {choice(self.faddres_de)} {randint(1, 100)}')
            elif self.f == '':
                return(f'{choice(self.faddres_de)} {randint(1, 100)}')
        
        else:
            return('Error №2! Unknow region!')
    
    def fake_email(self):
        return(f'{choice(self.email)}{choice(self.email_index)}')
    
    def fake_pass(self):
        return(f'{choice(self.fpassword)}fu{randint(10000000, 99999999)}{choice(self.fpassword)}')
    
    def fake_dob(self):
        year = randint(1920, 2024)
        morth = randint(0, 12)
        if morth == 2:
            day = randint(0, 28)
            return(f'{day}.{morth}.{year}')
        else:
            day = randint(0, 30)
            return(f'{day}.{morth}.{year}')
        
    def fake_city(self):
        gn = self.reg
        if gn == 'ru':
            return(f'г.{choice(self.fcity_ru)}')
        elif gn == 'en':
            return(f'{choice(self.fcity_en)} city')
        elif gn == 'de':
            return(f'{choice(self.fcity_de)}')

        else:
            return('Error №2! Unknow region!')
        
    def fake_banknumber(self):
        return(f"{randint(1000, 1500)} {randint(1000, 3000)} {randint(1000, 9000)} {randint(1000, 9000)}")
    
    def fake_login(self):
        return(choice(self.login))
    
    def fake_link(self):
        return(f'{choice(self.fname_link)}.{choice(self.findex_link)}')
    
    def fake_autonum(self):
        gn = self.reg
        if gn == 'ru':
            return(f'{choice(self.frus_num)}{randint(100, 999)}{choice(self.frus_num)}{choice(self.frus_num)}{randint(10, 990)}')
        elif gn == 'en':
            return(f'{choice(self.fde_num)}{choice(self.fde_num)}{choice(self.fde_num)}-{randint(100, 999)}')
        elif gn == 'de':
            return(f'{choice(self.fde_num_index)} {choice(self.fde_num)}{choice(self.fde_num)}{randint(1000, 9999)}')

    def fake_text(self):
        gn = self.reg
        if gn == 'ru':
            return(f'{choice(self.fpartone_text_ru)} {choice(self.fparttwo_text_ru)} {choice(self.fpartthree_text_ru)}')
        elif gn == 'en':
            return(f'{choice(self.fpartone_text_en)} {choice(self.fparttwo_text_en)} {choice(self.fpartthree_text_en)}')
        elif gn == 'de':
            return(f'{choice(self.fpartone_text_de)} {choice(self.fparttwo_text_de)} {choice(self.fpartthree_text_de)}')      
        else:
            return('Error №2! Unknow region!')
    
    def fake_job(self):
        gn = self.reg
        if gn == 'ru':
            return(choice(self.fjob_ru))
        elif gn == 'en':
            return(choice(self.fjob_en))
        elif gn == 'de':
            return(choice(self.fjob_de))
        else:
            return('Error №2! Unknow region!')