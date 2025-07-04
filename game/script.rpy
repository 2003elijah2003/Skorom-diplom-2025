# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Гоблин")
define kb = Character("Кот-баюн")
define pr = Character("Принцесса")


$ pointgoblin = 0
$ lovegoblin = 0
$ lovekot = 0

transform left:
    xalign 0.20
    yalign 0.50

transform right:
    xalign 0.80
    yalign 0.50


#Declare music

define audio.gamemusic = "audio/osnov.mp3"

# The game starts here.


label start:
    play music gamemusic
    $ pointgoblin = 0
    scene pz0
    pause 1.5 
    show гоблин at left
    with Dissolve (2)
    g "Не то чудо из чудес, что мужик упал с небес, а то чудо, как он туда залез."  
    g "Это призказка, а сказка чередом пойдёт о..."
    g "Хм.."
    menu:
        "Какую бы сказку мне рассказать?"
        "Про мужичка, который взобрался на небо!":
            jump my_na_nebe
        "Про мужичка, который упал с неба!":  
            jump my_na_nebe   
   

    return

# Сказки

label my_na_nebe:

    $ lovegoblin = 0
    scene pz0
    show гоблин 
    g "Это моя любимая сказка!"
    g "И я буду рад тебе её рассказать..."
    g "За небольшую плату."
    g "У верен ты разберёшься, что от тебя требуется по ходу дела."
    hide гоблин
    $ max_time = 40
    $ ww, hh = 4, 3
    scene paper
    call memoria_game
    scene pz0 
    show гоблин
    with Dissolve (2)
    pause 0.2
    g "Ты справился и заслужил сказку!"
    g "Пустил мужик петуха в подвал; петух там нашел горошинку. Мужик увидел находку, вынул петуха, а горошинку полил водою. Вот она и начала расти; росла-росла — выросла до́ полу."
    g "Мужик пол прорубил, горошинка опять начала расти; росла-росла — доросла до потолка. Мужик потолок прорубил, горошинка опять росла-росла — доросла до крыши."
    g "Оу, я забыл предупредить, что в этой сказке часто будет повторяться слово - мужик. Всё таки он главный герой этой истории."
    g "Всё, я продолжаю!"
    g "Мужик и крышу разобрал, стала горошинка еще выше расти; росла-росла — доросла до небушка."
    g "Мужик и полез на небушко, лез-лез, насилу влез. Входит в хоромы: везде такое загляденье, что он чуть было глаз не проглядел! Середи хором стоит печка, в печке и гусятины, и поросятины, и пирогов — видимо-невидимо! Одно слово сказать — чего только душа хочет, все есть!"
    g "Сторожит ту печку коза о семи глазах. Мужик догадался, что надобно делать, и стал про себя приговаривать: «Засни, глазок, засни, глазок!»"
    g "Один глаз у козы заснул. Мужик стал приговаривать погромче: «Засни, другой, засни, другой!» И другой глаз заснул. Таким побытом все шесть глаз у козы заснули; а седьмого глаза, который был у козы на спине, мужик не приметил и не заговорил."
    g "Недолго он думал, полез в печку, напился-наелся, насахарился; вылез оттуда и лег на лавочку отдохнуть. Пришел хозяин, а коза про все ему и рассказала: вишь, она все-то видела седьмым глазком. Хозяин осердился, кликнул своих слуг, и прогнали мужика взашеи."
    g "Побрел он к тому самому месту, где была горошинка: глянул — нет горошинки."
    g "Начал собирать паутину, что летает летом по воздуху; собрал паутину и свил веревочку; зацепил эту веревочку за край неба и стал спускаться. Спускался-спускался, хвать — веревочка вся, а до земли еще далеко-далеко; он перекрестился — и бух!"
    g "Летел-летел и упал в болото. Долго ли, коротко ли сидел он в болоте (а сидел он в болоте по самую шею), только вздумалось утке на его голове гнездо свить; свила гнездо и положила яйца."
    g "Мужик ухитрился, подкараулил утку и поймал ее за хвост. Утка билась, билась и вытащила-таки мужика из болота. Он взял и утку и яйца, принес домой и рассказал про все жене."
    g "На этом сказочке конец."
    g "Хочешь послушать ту сказку, которую не выбрал в начале?"
    menu:
        "Готов послушать?"
        "Конечно!":
            $ lovegoblin += 1
            g "И я рад тебе её рассказать!"
        "Да...":  
            g "Твой энтузиазм заразителен..."

    g "Но прежде...Тебе не кажется, что чего-то нехватает?"
    g "Я обсалютно уверен, что пейзаж позади меня должен быть поярче... Хм..."
    hide гоблин
    menu:
        "..."
        "Я помогу!":
            scene pz000
            $pazgame(1)
    scene bg0
    show гоблин
    g "О-о, ты большой молодец! Теперь я с большей охотой расскажу вторую сказку."
    g "Пустил мужик петуха в подвал; петух там нашел горошинку..."
    menu:
        "..."
        "И горошинка выросла до самого неба?":
            g "Да! Как ты мог это знать?"
            $ lovegoblin += 1
    g "Вообщем...Мужик полез на небушко, лез-лез, насилу влез. Входит в хоромы: везде такое загляденье. Середи хором стоит печка, в печке и гусятины, и поросятины, и пирогов — видимо-невидимо! Одно слово сказать — чего только душа хочет, все есть!"
    menu:
        "..."
        "А хоромы охраняет коза с семью глазами?":
            g "Да! Как ты мог это знать?"
            g "А теперь, когда ты прекратил меня перебивать, я продолжу."
        "А хоромы охраняет коза с девятью глазами?":
            g "А вот и нет!"
            g "Там стояла коза с семью глазами!"
            g "Вот! Ты не знаешь эту сказку... А раз я тебе рассказываю новую сказку..."
            hide гоблин
            $ max_time = 40
            $ ww, hh = 4, 3
            scene paper
            call memoria_game
            scene bg0 
            show гоблин
            with Dissolve (2)
    g "Так на чём я остановлся? Ах, точно!"
    g "Сторожит ту печку коза о семи глазах. Мужик догадался, что надобно делать, и стал про себя приговаривать: «Засни, глазок, засни, глазок!»"
    g "Один глаз у козы заснул. Мужик стал приговаривать погромче: «Засни, другой, засни, другой!» И другой глаз заснул. Таким побытом все шесть глаз у козы заснули; а седьмого глаза, который был у козы на спине, мужик не приметил и не заговорил."
    g "Недолго он думал, полез в печку, напился-наелся, насахарился; вылез оттуда и лег на лавочку отдохнуть. Пришел хозяин, а коза про все ему и рассказала: вишь, она все-то видела седьмым глазком. Хозяин осердился, кликнул своих слуг, и прогнали мужика взашеи."
    g "Побрел он к тому самому месту, где была горошинка: глянул — нет горошинки."
    g "Начал собирать паутину, что летает летом по воздуху; собрал паутину и свил веревочку; зацепил эту веревочку за край неба и стал спускаться. Спускался-спускался, хвать — веревочка вся, а до земли еще далеко-далеко; он перекрестился — и бух!"
    menu:
        "..."
        "...И упал в болото...":
            $ lovegoblin += 1
            g "Ты как всегда очень проницателен..."
            g "И я хочу похвалить тебя..."
            hide гоблин
            $ max_time = 40
            $ ww, hh = 4, 4
            scene paper
            call memoria_game
            scene bg0 
            show гоблин
            with Dissolve (2)
        "....И упал в лужу...":
            g "Конечно же нет!"
            g "Он бы умер, упав в лужу. Не хватило бы массы смегчающей падения... Я так думаю. В школе я прогуливал уроки чаровничества, а не физики..."
            g "И если ты заскучал, можешь разобраться с этим, и я продолжу."
            hide гоблин
            $ max_time = 40
            $ ww, hh = 4, 4
            scene paper
            call memoria_game
            scene bg0 
            show гоблин
            with Dissolve (2)
    g "Теперь, когда ты развеялся, я продолжу."
    g "Летел-летел и упал в болото. Долго ли, коротко ли сидел он в болоте (а сидел он в болоте по самую шею), только вздумалось утке на его голове гнездо свить; свила гнездо и положила яйца."
    g "Мужик ухитрился, подкараулил утку и поймал ее за хвост. Утка билась, билась и вытащила-таки мужика из болота. Он взял и утку и яйца, принес домой и рассказал про все жене."
    g "На этом сказочке конец."
    
    if lovegoblin == 3:
        g "Что ж, провести тебя оказалось не так-то просто."
        g "Мне очень приятно, что ты слушал внимательно."
    else:
        g "Мог бы и не перебивать меня!"
        g "Ведь, сказка с начала сказывается, до конца слушается, в середине не перебивается."
    hide гоблин
    with fade
    jump sivko_burko

    return


label sivko_burko:

    scene pz4
    show гоблин at left
    show кот-баюн at right
    with Dissolve (2)
    kb "Привет, старик! Что ты тут делаешь?"
    g "Я рассказываю сказки."
    kb "И твой слушатель не заснул? Ого!"
    menu:
        "..."
        "Мне понравилось слушать.":
            g "Ещё бы, я оттачивал это ремесло десятилетиями!"
            kb "Я бы предположил, что столетиями."
        "Согласен, я сдерживал зевки.":
            g "Я и не хотел показывать весь свой талант не благодарной публике."
            kb "Покажи ты весь свой талант, бедолага точно бы заснул"
    kb "В любом случае, у меня тоже припасена сказочка."  
    menu:
        "..."
        "За небольшую услугу?":
            kb "За небольшую услугу)."
    
    hide гоблин
    hide кот-баюн
    $ max_time = 50
    $ ww, hh = 4, 4
    scene paper
    call memoria_game
    scene pz4
    show кот-баюн
    with Dissolve (2)
    kb "Время сказки!"
    kb "В некотором царстве, в некотором государстве жил-был такой старичок, который трёх своих сынов научил грамоте и всему книжному."   
    kb "Старшие два брата какие были молодцы: и рослы, и дородны! А меньшой, Ванюша, — как недоросточек, как защипанный утёночек, гораздо поплоше."
    kb "— Ну, детки, когда помру я, приходите ко мне на могилку читать."
    kb "— Хорошо, хорошо, батюшка! — отвечали дети."
    kb "Пришло время, старик и помер."
    kb "В ту пору от царя пришло известие, что дочь его Елена-царевна Прекрасная приказала выстроить себе храм о двенадцать столбов, о двенадцать венцов."
    kb "Сядет она в этом храме на высоком троне и будет ждать жениха, удалого молодца, который бы на коне-летуне с одного взмаха поцеловал её в губки."
    kb "— Братья, — говорит Ванюша, — отец умер; кто из нас пойдёт на могилу читать?"
    kb "— А кого охота берёт, тот пускай и идёт! — отвечали братья; Ваня пошёл. А старшие знай себе коней объезжают, кудри завивают, фабрятся, бодрятся родимые…"
    kb "Пришла другая ночь."
    kb "— Братья, я прочитал, — говорил Ваня, — ваша очередь; который пойдёт?"
    kb "— А кто охоч, тот и читай, а нам дело делать не мешай."
    kb "Сами заломили шапки, гикнули, ахнули, полетели, понеслись, загуляли в чистом поле! Ванюша опять читал; на третью ночь то же. А братья выездили коней, расчесали усы, собираются нынче-завтра пытать своё удальство перед очами Елены Прекрасной."
    kb "— Брать ли меньшего? — думают. — Нет, куда с ним! Он и нас осрамит и людей насмешит; поедем одни."
    kb "Поехали; а Ванюше очень хотелось поглядеть на Елену-царевну Прекрасную; заплакал он, больно заплакал и пошёл на могилу к отцу."
    kb "Услышал его отец, вышел к нему, стряхнул с чела сыру землю и говорит:"
    kb "— Не тужи, Ваня, я твоему горю пособлю."
    kb "Тотчас старик вытянулся, выпрямился, свистнул-гаркнул молодецким голосом, соловейским посвистом; откуда ни взялся — конь бежит, земля дрожит, из ноздрей, из ушей пламя пышет; порхонул и стал перед стариком как вкопанный."
    kb "Влез Ваня коню в одно ушко, вылез в другое и сделался таким молодцом, что ни в сказке сказать, ни пером написать! Сел на коня, подбоченился и полетел, что твой сокол, прямо к палатам Елены-царевны."
    kb "Размахнулся, подскочил — двух венцов не достал; завился опять, разлетелся, скакнул — одного венца не достал; ещё закружился, ещё завертелся, как огонь проскочил мимо глаз, метко нацелил и прямо в губки чмокнул Елену Прекрасную!"
    kb "Прискакал на отцову могилу, коня пустил в чистое поле, а сам в землю да поклон, да просит совета родительского; старик и посоветовал. Домой пришёл Иван, как нигде не бывал; братья рассказывают: где были, что видели; а он как впервой слышит."
    kb "На другой день опять сбор; и бояр и дворян у княжих палат глазом не окинешь! Поехали старшие братья; пошёл и меньшой брат пешечком, скромно, смирно, словно не он целовал царевну, и сел в дальний уголок."
    kb "Елена-царевна кликает жениха, хочет его всему свету показать, хочет ему полцарства отдать, а жених не является! Его ищут между боярами, меж генералами, всех перебрали — нету! А Ваня глядит, ухмыляется, улыбается и ждёт, что сама невеста к нему придёт."
    kb " — Я полюбился ей молодцом, теперь она полюби меня в кафтане простом."
    kb "Встала сама, повела ясным оком, осветила всех, увидела и узнала своего жениха, посадила его с собой и скоро с ним обвенчалась; а он-то, какой стал умный да смелый, а какой красавец!"
    hide кот-баюн
    pause 1.5
    show гоблин at left
    with Dissolve (2)
    show кот-баюн at right
    with Dissolve (2)
    g "Должен согласиться, что это действительно хорошая сказка... Удивительно, что именно ты её рассказал."
    g "Кстати, дружеский совет, кхм, совет настоящего мастера - слушать сказку, смотря на цветную иллючтрацию, более приятно."
    kb "Ах, ты на счёт пейзажа... С некоторого времени у меня проблема. Все краски пропали."
    g " Я знаю того, кто поможет!"
    hide гоблин
    hide кот-баюн
    menu:
        "..."
        "Я помогу!":
            scene pz44
            $pazgame(4)
    scene bg1
    show гоблин at left
    show кот-баюн at right
    kb "О-о, твой друг настоящий волшебник!"
    g "Вот только в сказках мало что смыслит."
    kb "Уверен, это не так. Кстати, вам понравилась моя сказка?"
    menu:
        "..."
        "Понравилось!": 
            kb "Хоть я и неоттачивал своё мастерство столетиями, но получается у меня не плохо."
            g "Я мог бы и лучше."
            g "И мне кажется наш друг слушал вполуха. И вообще мало, что понимает в волшебных историях!"
        "Не понравилось":
            g "Хе-хе, наш друг, в отличии от меня, ничего в себе не держит."
            g "Не переживай, Баюн. У тебя в переди «столетия» практики."
            g "Но справедливо заметить, что слушатель может вообще ничего не смыслить в волшебных историях!"
    kb "Хорошо, ты можешь проверить его знания. Но я ни на секнду не сомневаюсь, что наш друг справится!."
    hide кот-баюн
    
    jump test1
        
    return

label test1:
    show гоблин at left
    
    g "Оу, люблю таких уверенных глупцов!"
    g "Начнём"
    menu:
        "С чего начинается сказка?"
        "С самого интересного!":
            $ pointgoblin = 0
            "..."        
        "С Присказки или зачина":
            $ pointgoblin += 2
            "С присказки или зачина"
    
    g "Ты сделал выбор"
    menu:
        "Сказки бывают..."
        "Волшебные, бытовыи и о животных":
            $ pointgoblin += 2
            "..."        
        "Сказочными!":
            $ pointgoblin = 0
            "..." 

    g "Ты сделал выбор"
    menu:
        "Но так же сказки могут быть.."
        "Авторские и народные":
            $ pointgoblin += 2
            "..."        
        "Невероятно скучными":
            $ pointgoblin = 0
            "..." 

    g "Время подвести итоги."
    if pointgoblin == 6:
        g "Ты справился!"
        g "Невероятно"
    else:
        g "Упс..."
        g "Это было плохо"
        show кот-баюн at right
        kb "Эй-эй, старик."
        kb "Он только учиться!"
        hide гоблин
        kb "И так, слушай."
        kb "Сказка начинается с присказки или зачина."
        kb "Присказка - это ритмична прибаутка, обычно никак не связаная с основным сюжетом в самой сказке и может вообще отсутствовать"
        kb "Русские народные сказки разделяют на сказки о животных, волшебные и бытовые сказки."
        kb "У сказок может быть конкретный автор. Тогда это будет авторской сказкой."
        kb "На этот раз ты готов!"
        jump test1
    kb "На этом я буду прощаться, мне пора идти дальше."
    g "Мы тоже пойдём."
    hide кот-юаюн
    hide гоблин
    with fade
    jump princessa
    return
    
label princessa:
    $ zagadki = False
    scene pz5
    pause 1.5           
    show гоблин at left
    show принцесса at right    
    with Dissolve (2)
    g "Ваше величество!"
    pr "На самом деле «высочество». Но я здесь не как принцесса."
    pr "Я увидела чем вы тут занимаетесь, и захатела к вам."
    g "Мы рассказываем друг другу сказки. Ты хочешь рассказать или послушать?"
    pr "Я же принцесса! Конечно я хочу чтоб для меня что-то сделали, а не я."
    g "Хе-хе, ну а я сказочник! И конечно я хочу рассказать сказку."
    g "Я начинаю."
    g "Пустил мужик петуха в подвал; петух там нашел горошинку. Мужик увидел находку, вынул петуха, а горошинку полил водою. Вот она и начала расти; росла-росла — выросла до́ полу."
    menu:
        "..."
        "Слушать дальше":
            g "Мужик пол прорубил, горошинка опять начала расти; росла-росла — доросла до потолка. Мужик потолок прорубил, горошинка опять росла-росла — доросла до крыши."
            g "Мужик и крышу разобрал, стала горошинка еще выше расти; росла-росла — доросла до небушка."
            g "Мужик и полез на небушко, лез-лез, насилу влез. Входит в хоромы: везде такое загляденье, что он чуть было глаз не проглядел! Середи хором стоит печка, в печке и гусятины, и поросятины, и пирогов — видимо-невидимо! Одно слово сказать — чего только душа хочет, все есть!"
            g "Сторожит ту печку коза о семи глазах. Мужик догадался, что надобно делать, и стал про себя приговаривать: «Засни, глазок, засни, глазок!»"
            g "Один глаз у козы заснул. Мужик стал приговаривать погромче: «Засни, другой, засни, другой!» И другой глаз заснул. Таким побытом все шесть глаз у козы заснули; а седьмого глаза, который был у козы на спине, мужик не приметил и не заговорил."
            g "Недолго он думал, полез в печку, напился-наелся, насахарился; вылез оттуда и лег на лавочку отдохнуть. Пришел хозяин, а коза про все ему и рассказала. Хозяин осердился, кликнул своих слуг..."
            pr "И хозяин схватил вора и приказал казнить? Я поступила бы точно также, если бы в мой замок вломились неотёсанные грабители."
            g "Э-э, нет... Всё было не так."
            pr "Неважно, мне не нравится эта сказка. Можешь не продолжать."
            pr "Я же принцесса! Мне не интересны сказки про деревенских мужичков.., которые ещё и воры."
            g "Мужик не воришка! Это же сказочная ситуация! Ладно-ладно. Другую сказку про принцесс, так другую."
        "Кхм-кхм...":
            g "Что такое?"
            pr "Я согласна с этой реакцией. Я не хочу слушать крестьянские сказки. Я же принцесса!"
            g "Хм... Будь по вашему, ваше высочество."
    g "Не силён я в таких сказках, но раз публика требует..." 
    g "...Мой новый друг мне поможет!"
    menu:
        "..."
        "Мне кажется, у меня опять нет выбора":
            g "Только не забудь о..."

    hide гоблин
    hide принцесса
    $ max_time = 100
    $ ww, hh = 8, 4 #84
    scene paper
    call memoria_game
    scene pz5
    pause 1.5
    show гоблин at left
    show принцесса at right
    with Dissolve (2)
    menu:
        "..."
        "В некотором царстве, в некотором государстве жил-был царь, и была у него дочка. Говорит она раз отцу":
            pr "— Прикажи, батюшка, кликнуть клич: пусть к нам едут со всех сторон молодцы. Они будут загадки загадывать, а я буду отгадывать. Чьи загадки отгадаю, тому голову рубить. Чьи не отгадаю, за того пойду замуж, пускай хоть последним пастухом будет!"
    menu:
        "..."
        "Согласился царь.":
            "Кликнули клич. Съехались со всех сторон молодцы, каждый со своими загадками. Начнёт какой из них загадывать загадку, а царевна не дослушает и уже кричит отгадку."
    menu:
        "..."
        "А жил в том царстве-государстве старик. У него было три сына. Младшего Иванушкой звали.":
            "— Благословляй, батюшка! Я пойду к царю загадывать загадки!"
    menu:
        "..."
        "Благословил старик сына.":
            "Сел Иванушка на старую клячу-водовозку и поехал. Видит — на дороге ржавое копьё лежит."
    menu:
        "..."
        "Поднял копьё и поехал дальше":
            "Ехал он, ехал — смотрит: забрался бык в овёс, ест да топчет его."
            menu:
                "..."
                "Прогнал быка.":
                    $ zagadki = True
                    "Слез Иванушка с лошади, вырвал пук овса, махнул им, как кнутом, и выгнал быка из овса."
                    "Поехал он дальше. Смотрит — навстречу ему по дороге змея ползёт. Иванушка заколол её копьём."
                    "Приезжает к царю; его приняли и велят загадывать загадки."
                    "— Ехал я к вам, вижу на дороге добро, в добре-то добро же, я взял добро-то да добром из добра и выгнал; добро от добра и из добра убежало."
                    "Царевна хватила книжку, смотрит: нету этой загадки; не знает разгадки и говорит отцу:"
                    pr "— Батюшка! У меня сегодня головушка болит, мысли помешались; я завтра разгадаю."
                    "Отложили до завтра. Ивану-дураку отвели комнату. Он вечером сидит, покуривает трубочку; а царевна выбрала верную горнишну, посылает её к Ивану-дураку:"
                    pr "— Поди, спроси у него, что́ это за загадка; сули ему злата и серебра, чего угодно."
                    "Горнишна приходит, стучится; Иван-дурак отпёр двери, она вошла и спрашивает загадку, сулит горы золота и серебра. Иван-дурак и говорит:"
                    "— На что мне деньги! У меня своих много. Пусть царевна простоит всю ночь не спавши в моей горнице, дак скажу загадку."
                    "Царевна услышала это, согласилась, стояла всю ночь — не спала. Иван-дурак утром сказал загадку, что выгнал из хлеба лошадь. И царевна разгадала."
                    "Иван-дурак стал другую загадывать:"
                    "— Ехал я к вам, на дороге вижу зло, взял его да злом и ударил, зло от зла и умерло."
                    "Царевна опять схватила книжку, не может разгадать загадку и отпросилась до утра. Вечером посылает горнишну узнать у Ивана-дурака загадку. И опять всю ночь в гонице у Ивана-дурака простояла, а на утро разгада, что копьём была змея убита."
                    "Третью загадку Иван-дурак просто так не стал загадывать, а велел собрать всех бояр и загадал, как царевна не умела отгадывать те загадки и посылала к нему горнишну подкупать на деньги."
                    "Царевна не могла догадаться и этой загадки; опять к нему спрашивать — сулила серебра и золота сколько угодно и хотела отправить домой на прогоне. Не тут-то было!"
                    "Опять простояла ночь не спавши; он как сказал ей, о чём загадка, — ей разгадывать-то нельзя; о ней, значит, узнают, как и те загадки она выпытывала у Ивана-дурака. И ответила царевна:"
                    pr "— Не знаю!!!"
                    "Вот весёлым пирком, да и за свадебку: Иван-дурак женился на ней; стали жить да быть. Тут и сказочки конец."
                "Не стал выгонять быка.":
                    "Поехал он дальше. Смотрит — навстречу ему по дороге змея ползёт. Иванушка обошёл её и дальше поехал."
            
        "Не стал поднимать копья и поехал дальше":
            "Ехал он, ехал — смотрит: забрался бык в овёс, ест да топчет его. Усмехнулся Иванушка и поехал дальше"
            "Поехал он дальше. Смотрит — навстречу ему по дороге змея ползёт. Иванушка обошёл её и дальше поехал."
            "Долго ли, коротко ли — подъехал он к реке и думает"
            menu:
                "..."
                "Поехать ли...":
                    "Не стал терять времени и снова отправился в путь."
                    "Приехал к царскому дворцу и говорит:"
                    "— Ведите меня к вашей царевне! Буду ей загадки загадывать!"
                    "Привели его, он и загадывает."
                    menu:
                        "..."
                        "Рыжая плутовка, хитрая да ловкая!":
                            "Царевна смеялась о-о-очень долго"
                        "Если щёки я надую, листья с ветки сдую!":
                            "Царевна смеялась о-о-очень долго"
                        "Жёлтый глаз, вокруг реснички, погадайже мне, сестричка!":
                            "Царевна смеялась о-о-очень долго"
                    "К вечеру Ванюшку и казнили."    
                "Остаться на ночь ли...":
                    "Отпустил он свою лошадь на траву пастись, а сам улёгся в старую лодку, что была у берега привязана, и заснул."
                    "Утром Иванушка проснулся. Видит — на воде пена собралась. Снял он с воды пену, умылся. Подошёл к своей лошади и утёрся её гривой вместо полотенца."
                    "Сел на лошадь и поехал дальше."
                    "— Ведите меня к вашей царевне! Буду ей загадкe загадывать!"
                    "Привели к царевне."
                    "— Ехал я к вам, и застигла меня в пути тёмная ночь. Остановился ночевать. Лёг спать не на небе, не на земле, не в избе, не на улице, не в лесу, не в поле. Утром проснулся, умылся не росой, не водой; утёрся не тканым, не вязаным. Какая ваша отгадка будет?"
                    "Царевна думала-думала — никак отгадать не может. Схватила она толстую книжку, стала искать в ней отгадку. Нету в книжке такой отгадки!"
                    "Говорит тогда отцу:"
                    pr "— Ох, батюшка! У меня сегодня головушка болит, мысли помешались… Я завтра отгадаю."
                    "Царь велел отложить отгадки до завтра. Отвели Иванушку на ночь в комнату, велели никуда не уходить. Достал он краюшку хлеба, сидит и уплетает её."
                    "Рассердилась царевна, не знает, что и делать. И загадку отгадать не может и замуж за простого мужика идти не хочет. Думала она, думала и надумала недоброе дело."
                    "Приказала царевна Иванушку к себе в горницу просить: хочет пряниками да винами сладкими угостить. Иванушка пришёл. Усадила его царевна за стол, стала потчевать. А сама незаметно ему в чарку сонного зелья подсыпала. Выпил Иванушка и крепко заснул."
                    "Тут царевна позвала свою верную служанку, одарила её богатыми подарками и велела увезти Иванушку подальше и бросить в топкое болото, чтобы ни слуху ни духу его больше не было!"
                    "Отвезли Иванушку и бросили в болото, в самую трясину…"
    g "Браво!"
    g "Я заслушался, а у тебя талант!"            
    pr "Я под впечатлением!!!...Но... Мне кое-что не понравилось."
    pr "Я не вредничаю, просто... Твоей истории нехватает красок..."     
    hide гоблин
    hide принцесса
    menu:
        "..."
        "Я исправлюсь, ваше высочество!":
            scene pz55
            $pazgame(5)
    scene bg2
    show гоблин at left
    show ghbywtccf at right    
    pr "Вот теперь всё прекрасно."   
                

    return