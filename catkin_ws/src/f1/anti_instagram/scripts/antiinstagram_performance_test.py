from anti_instagram import wrap_test_main, logger, random_image, AntiInstagram
import timeit


def anti_instagram_test_performance():
    logger.info('This is going to test the performance of algorithm 1 and 2')

    #### TEST CALC TIMING ####
    calcuateTransformOnRandomImg()
    applyTransformOnRandomImg()


def setup():
    img = random_image(480, 640)
    ai = AntiInstagram()
    return ai, img

def applyTransformOnRandomImg():
    n = 3
    tn = timeit.timeit(stmt='ai.applyTransform(img)',
        setup='from __main__ import setup; ai,img=setup()',
        number=n
        )
    t = tn / n
    logger.info("Average Apply Transform Took: %.1f ms " % (t * 1000))

def calcuateTransformOnRandomImg():
    n = 3
    tn = timeit.timeit(stmt='ai.calculateTransform(img,True)',
                    setup='from __main__ import setup; ai,img=setup()',
                    number=n)

    t = tn / n
    logger.info("Average Calculate Transform Took: %.1f ms" % (t * 1000))



if __name__ == '__main__':
    wrap_test_main(anti_instagram_test_performance) 
