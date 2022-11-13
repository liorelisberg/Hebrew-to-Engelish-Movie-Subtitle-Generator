import tensorflow as tf
import tensorflow_text

print(tf.__version__)
print(tensorflow_text.__version__)

saved_model_path = "AI\Model\Translator"

def get_translator():
    # Loading the model from a path on localhost.
    another_strategy = tf.distribute.MirroredStrategy()
    with another_strategy.scope():
        load_options = tf.saved_model.LoadOptions(experimental_io_device='/job:localhost')
        model = tf.saved_model.load(saved_model_path, options=load_options)
        # model.translate(['test']) # warm-up
        return model

def translate(t,source):   
    empty_padding ='[UNK]'
    if type(source) is not str:
        raise TypeError(f"source sequecene needs to be str. source: {source}, source type:{type(source)}")
    
    if source is None:
        return ""
    
    target = t.translate([source])
    target = str(target[0].numpy().decode())
    
    splitted_target = target.split()
    
    if splitted_target[0] == empty_padding:
        splitted_target[0] = ""
        
    if splitted_target[-1] == empty_padding:
        splitted_target[-1] = ""
    
    target = str.join(' ',splitted_target)
    target = target.replace(empty_padding,'_')
    return target
      
# def test():
#     t = get_translator()

#     # heb_word1 = translator.translate(['hello'])
#     heb_word1 = translate(t,'hello')
#     print(heb_word1)
#     print()
#     # heb_word2 = translator.translate(['how are you today?'])
#     heb_word2 = translate(t,'how are you today?')
#     print(heb_word2)
#     print()
#     # heb_word3 = translator.translate(['you are my best friend'])
#     heb_word3 = translate(t,'you are my best friend')
#     print(heb_word3)
#     print()
    
# if __name__ == '__main__':
#     test()