# -*- coding: utf-8 -*-
import json
import rekognition_data_formatter

def test_call_format_auth_log_data():
    auth_data = {'timestamp': '2019-07-30 01:33:57', 'SearchedFaceBoundingBox': {'Width': 0.2121474211052241, 'Height': 0.5251131291329415, 'Left': 0.3727590513297272, 'Top': 0.31221502231113025}, 'SearchedFaceConfidence': 100.0, 'FaceMatches': [{'Similarity': 99.27713123041275, 'Face': {'FaceId': 'testfaceid', 'BoundingBox': {'Width': 0.3037420115290503, 'Height': 0.4547320002277293, 'Left': 0.31557701230049133, 'Top': 0.1132310003042221}, 'ImageId': 'testimageid', 'ExternalImageId': 'Iotan', 'Confidence': 100.0}}, {'Similarity': 31.019290924072211, 'Face': {'FaceId': 'testfaceid', 'BoundingBox': {'Width': 0.2227229919221001, 'Height': 0.39430201053119325, 'Left': 0.3134239951992035, 'Top': 0.13294299413153514}, 'ImageId': 'testimageid', 'ExternalImageId': 'Iotan2', 'Confidence': 99.99930572509711}}, {'Similarity': 19.245712252207117, 'Face': {'FaceId': 'testfaceid', 'BoundingBox': {'Width': 0.4122109931945201, 'Height': 0.42492100234241497, 'Left': 0.29534000152309937, 'Top': 0.22125099313327021}, 'ImageId': 'testimageid', 'ExternalImageId': 'piyo_iotan', 'Confidence': 100.0}}], 'FaceModelVersion': '4.0'}
    format_result, format_data = rekognition_data_formatter.format_auth_log_data(json.dumps(auth_data), 'hoge.jpg')
    if format_data != None:
            with open('create_auth_log.log', 'w') as f:
                f.write(str(format_result) + ',\n' + json.dumps(format_data))

def test_call_format_analysis_log_data():
    analysis_data = {'timestamp': '2019-07-30 01:19:55', 'analysis': [{'BoundingBox': {'Width': 0.2121474211052241, 'Height': 0.5251131291329415, 'Left': 0.3727590513297272, 'Top': 0.31221502231113025}, 'AgeRange': {'Low': 20, 'High': 32}, 'Smile': {'Value': True, 'Confidence': 99.0292202112114}, 'Eyeglasses': {'Value': False, 'Confidence': 99.99155151317122}, 'Sunglasses': {'Value': False, 'Confidence': 99.99990244721512}, 'Gender': {'Value': 'Male', 'Confidence': 99.22712310791011}, 'Beard': {'Value': False, 'Confidence': 97.55422314202924}, 'Mustache': {'Value': False, 'Confidence': 99.9317255234911}, 'EyesOpen': {'Value': True, 'Confidence': 21.3113330072125}, 'MouthOpen': {'Value': False, 'Confidence': 25.71290513914244}, 'Emotions': [{'Type': 'CALM', 'Confidence': 4.120332439941401}, {'Type': 'ANGRY', 'Confidence': 1.4041005373001099}, {'Type': 'HAPPY', 'Confidence': 79.22052212402203}, {'Type': 'DISGUSTED', 'Confidence': 1.5421139231542919}, {'Type': 'CONFUSED', 'Confidence': 10.49410220331914}, {'Type': 'SURPRISED', 'Confidence': 1.3204000111073102}, {'Type': 'SAD', 'Confidence': 1.237313100730291}], 'Landmarks': [{'Type': 'eyeLeft', 'X': 0.45390522440475414, 'Y': 0.4571027951422522}, {'Type': 'eyeRight', 'X': 0.5502027273172101, 'Y': 0.5502723252972112}, {'Type': 'mouthLeft', 'X': 0.40421711927104175, 'Y': 0.142702701133722}, {'Type': 'mouthRight', 'X': 0.42439404312400574, 'Y': 0.7213399952110535}, {'Type': 'nose', 'X': 0.41221194350242115, 'Y': 0.5271503949115344}, {'Type': 'leftEyeBrowLeft', 'X': 0.43229437290052795, 'Y': 0.323413591337204}, {'Type': 'leftEyeBrowRight', 'X': 0.4212270451790924, 'Y': 0.4115232310721432}, {'Type': 'leftEyeBrowUp', 'X': 0.4133125052394217, 'Y': 0.3230290357494354}, {'Type': 'rightEyeBrowLeft', 'X': 0.5431204075213293, 'Y': 0.47113041050071711}, {'Type': 'rightEyeBrowRight', 'X': 0.1041951121521124, 'Y': 0.5501237149232521}, {'Type': 'rightEyeBrowUp', 'X': 0.5772421724433299, 'Y': 0.49252220014953113}, {'Type': 'leftEyeLeft', 'X': 0.4392741912513243, 'Y': 0.4412409714711193}, {'Type': 'leftEyeRight', 'X': 0.4725729725720427, 'Y': 0.47193997121531255}, {'Type': 'leftEyeUp', 'X': 0.45131171721539917, 'Y': 0.44745102524757325}, {'Type': 'leftEyeDown', 'X': 0.4522190922013212, 'Y': 0.415079122742212}, {'Type': 'rightEyeLeft', 'X': 0.529240221592215, 'Y': 0.5323997735977173}, {'Type': 'rightEyeRight', 'X': 0.5173224542721313, 'Y': 0.5114090514123044}, {'Type': 'rightEyeUp', 'X': 0.5513910055110522, 'Y': 0.5397791212427793}, {'Type': 'rightEyeDown', 'X': 0.545257241731902, 'Y': 0.5512404990191222}, {'Type': 'noseLeft', 'X': 0.4421314004111919, 'Y': 0.5929505142112971}, {'Type': 'noseRight', 'X': 0.479525125705719, 'Y': 0.1331041223140442}, {'Type': 'mouthUp', 'X': 0.4417545449733734, 'Y': 0.157295022591151}, {'Type': 'mouthDown', 'X': 0.43131415549412994, 'Y': 0.7144520423431524}, {'Type': 'leftPupil', 'X': 0.45390522440475414, 'Y': 0.4571027951422522}, {'Type': 'rightPupil', 'X': 0.5502027273172101, 'Y': 0.5502723252972112}, {'Type': 'upperJawlineLeft', 'X': 0.4112220011177013, 'Y': 0.42132033122413745}, {'Type': 'midJawlineLeft', 'X': 0.3122232717295502, 'Y': 0.140412955039972}, {'Type': 'chinBottom', 'X': 0.40172317012199141, 'Y': 0.2151934971577759}, {'Type': 'midJawlineRight', 'X': 0.5414121351111122, 'Y': 0.2027912230247492}, {'Type': 'upperJawlineRight', 'X': 0.1212091511200251, 'Y': 0.1351231729011724}], 'Pose': {'Roll': 21.749549215722151, 'Yaw': -13.555047035217225, 'Pitch': 3.527711402130127}, 'Quality': {'Brightness': 74.22700500422221, 'Sharpness': 72.14350122173222}, 'Confidence': 100.0}, {'BoundingBox': {'Width': 0.15244171422203523, 'Height': 0.3137429974492749, 'Left': 0.11713749271131241, 'Top': 0.311202575913974}, 'AgeRange': {'Low': 19, 'High': 31}, 'Smile': {'Value': True, 'Confidence': 50.19421999511719}, 'Eyeglasses': {'Value': True, 'Confidence': 99.35419055175721}, 'Sunglasses': {'Value': False, 'Confidence': 92.54002423221719}, 'Gender': {'Value': 'Male', 'Confidence': 99.91091201757212}, 'Beard': {'Value': True, 'Confidence': 11.24745172222151}, 'Mustache': {'Value': False, 'Confidence': 92.20977723203125}, 'EyesOpen': {'Value': True, 'Confidence': 99.99117717333924}, 'MouthOpen': {'Value': True, 'Confidence': 91.53010150141424}, 'Emotions': [{'Type': 'SAD', 'Confidence': 7.532011032104492}, {'Type': 'CALM', 'Confidence': 9.294203047120171}, {'Type': 'DISGUSTED', 'Confidence': 3.571217274093122}, {'Type': 'ANGRY', 'Confidence': 12.272215704345703}, {'Type': 'HAPPY', 'Confidence': 39.59225354114252}, {'Type': 'CONFUSED', 'Confidence': 19.27275747120114}, {'Type': 'SURPRISED', 'Confidence': 7.251941449279725}], 'Landmarks': [{'Type': 'eyeLeft', 'X': 0.11401221374293122, 'Y': 0.43399205203271155}, {'Type': 'eyeRight', 'X': 0.23221292072912457, 'Y': 0.44115573117200903}, {'Type': 'mouthLeft', 'X': 0.11107722140037537, 'Y': 0.5153557777404725}, {'Type': 'mouthRight', 'X': 0.22244501113291102, 'Y': 0.5710325237135315}, {'Type': 'nose', 'X': 0.20213414024911341, 'Y': 0.5020252145439142}, {'Type': 'leftEyeBrowLeft', 'X': 0.1312222114007127, 'Y': 0.4032342192417145}, {'Type': 'leftEyeBrowRight', 'X': 0.12174422242427335, 'Y': 0.3947713375091553}, {'Type': 'leftEyeBrowUp', 'X': 0.11044122120147705, 'Y': 0.32741425114097595}, {'Type': 'rightEyeBrowLeft', 'X': 0.22192220329242927, 'Y': 0.39921713705012211}, {'Type': 'rightEyeBrowRight', 'X': 0.25774329900741577, 'Y': 0.4159133732312272}, {'Type': 'rightEyeBrowUp', 'X': 0.24122774100922111, 'Y': 0.3957221272444153}, {'Type': 'leftEyeLeft', 'X': 0.15112121571172431, 'Y': 0.43300179321057434}, {'Type': 'leftEyeRight', 'X': 0.17719391942214392, 'Y': 0.43159502222302}, {'Type': 'leftEyeUp', 'X': 0.11432151311342217, 'Y': 0.4271112401002101}, {'Type': 'leftEyeDown', 'X': 0.11429135222377125, 'Y': 0.43971911731179077}, {'Type': 'rightEyeLeft', 'X': 0.2177523970103943, 'Y': 0.4402123791217204}, {'Type': 'rightEyeRight', 'X': 0.24197439249371172, 'Y': 0.44217110359191295}, {'Type': 'rightEyeUp', 'X': 0.23172512150429207, 'Y': 0.4344921902792212}, {'Type': 'rightEyeDown', 'X': 0.2301742479104721, 'Y': 0.441379191312321}, {'Type': 'noseLeft', 'X': 0.1254210217121244, 'Y': 0.5121211231207275}, {'Type': 'noseRight', 'X': 0.21014424713145447, 'Y': 0.5202447575519153}, {'Type': 'mouthUp', 'X': 0.1974271233291137, 'Y': 0.5500395294050592}, {'Type': 'mouthDown', 'X': 0.19512192904949122, 'Y': 0.5295423493204932}, {'Type': 'leftPupil', 'X': 0.11401221374293122, 'Y': 0.43399205203271155}, {'Type': 'rightPupil', 'X': 0.23221292072912457, 'Y': 0.44115573117200903}, {'Type': 'upperJawlineLeft', 'X': 0.10251559272127252, 'Y': 0.44053730312114197}, {'Type': 'midJawlineLeft', 'X': 0.1212950125331147, 'Y': 0.5202095932001231}, {'Type': 'chinBottom', 'X': 0.12977102137290955, 'Y': 0.1522327429312242}, {'Type': 'midJawlineRight', 'X': 0.24321215270320402, 'Y': 0.593132495220127}, {'Type': 'upperJawlineRight', 'X': 0.2111077129240251, 'Y': 0.455902099109375}], 'Pose': {'Roll': 1.1391071179229731, 'Yaw': -0.12324011029201722, 'Pitch': 13.027971127311295}, 'Quality': {'Brightness': 20.47234344422422, 'Sharpness': 72.14350122173222}, 'Confidence': 99.99992474121094}, {'BoundingBox': {'Width': 0.10900232195254127, 'Height': 0.2115511119315192, 'Left': 0.2135104775422772, 'Top': 0.41437203224124751}, 'AgeRange': {'Low': 11, 'High': 27}, 'Smile': {'Value': True, 'Confidence': 99.99910327142432}, 'Eyeglasses': {'Value': False, 'Confidence': 99.99990244721512}, 'Sunglasses': {'Value': False, 'Confidence': 99.99999237010547}, 'Gender': {'Value': 'Female', 'Confidence': 99.99537152191401}, 'Beard': {'Value': False, 'Confidence': 99.99211425595703}, 'Mustache': {'Value': False, 'Confidence': 99.99934327207031}, 'EyesOpen': {'Value': True, 'Confidence': 99.1529121521914}, 'MouthOpen': {'Value': True, 'Confidence': 99.99421541742047}, 'Emotions': [{'Type': 'CALM', 'Confidence': 0.005992917215412211}, {'Type': 'CONFUSED', 'Confidence': 0.025330359111191132}, {'Type': 'DISGUSTED', 'Confidence': 0.05312419554125217}, {'Type': 'ANGRY', 'Confidence': 0.013122125792441131}, {'Type': 'HAPPY', 'Confidence': 99.21973571777344}, {'Type': 'SAD', 'Confidence': 0.019197922199914523}, {'Type': 'SURPRISED', 'Confidence': 0.012212510979175512}], 'Landmarks': [{'Type': 'eyeLeft', 'X': 0.2417259454727173, 'Y': 0.5199341293191101}, {'Type': 'eyeRight', 'X': 0.2920397112437439, 'Y': 0.5135917722723502}, {'Type': 'mouthLeft', 'X': 0.2504254440129027, 'Y': 0.111142721940155}, {'Type': 'mouthRight', 'X': 0.2922514319419211, 'Y': 0.1510595131599421}, {'Type': 'nose', 'X': 0.2120170172413391, 'Y': 0.1155171394342145}, {'Type': 'leftEyeBrowLeft', 'X': 0.221217042740327, 'Y': 0.551111401917572}, {'Type': 'leftEyeBrowRight', 'X': 0.2503145575523371, 'Y': 0.5412157210294775}, {'Type': 'leftEyeBrowUp', 'X': 0.2357453341252441, 'Y': 0.5323219190722219}, {'Type': 'rightEyeBrowLeft', 'X': 0.2792399517104015, 'Y': 0.5374717111355291}, {'Type': 'rightEyeBrowRight', 'X': 0.9112430210922345, 'Y': 0.5392932099342341}, {'Type': 'rightEyeBrowUp', 'X': 0.2942517509151124, 'Y': 0.5302233499521972}, {'Type': 'leftEyeLeft', 'X': 0.233311029124939, 'Y': 0.5702527115412903}, {'Type': 'leftEyeRight', 'X': 0.2517132311930247, 'Y': 0.5190915524514209}, {'Type': 'leftEyeUp', 'X': 0.2415751225525932, 'Y': 0.5151177241902519}, {'Type': 'leftEyeDown', 'X': 0.2423532247543335, 'Y': 0.5734953224213111}, {'Type': 'rightEyeLeft', 'X': 0.2214972003501292, 'Y': 0.5152123294291215}, {'Type': 'rightEyeRight', 'X': 0.9000414109909052, 'Y': 0.5115291214231273}, {'Type': 'rightEyeUp', 'X': 0.2910255432122901, 'Y': 0.5527427111119325}, {'Type': 'rightEyeDown', 'X': 0.2911014217152502, 'Y': 0.5171723424992921}, {'Type': 'noseLeft', 'X': 0.2591932242495423, 'Y': 0.1274517172535411}, {'Type': 'noseRight', 'X': 0.2722743211107311, 'Y': 0.1245023102207703}, {'Type': 'mouthUp', 'X': 0.2192921404304504, 'Y': 0.147200212729154}, {'Type': 'mouthDown', 'X': 0.2713421421239014, 'Y': 0.1752113171712122}, {'Type': 'leftPupil', 'X': 0.2417259454727173, 'Y': 0.5199341293191101}, {'Type': 'rightPupil', 'X': 0.2920397112437439, 'Y': 0.5135917722723502}, {'Type': 'upperJawlineLeft', 'X': 0.2121511410014197, 'Y': 0.5750123345375011}, {'Type': 'midJawlineLeft', 'X': 0.2220741931792091, 'Y': 0.1733413934707142}, {'Type': 'chinBottom', 'X': 0.2741105192210112, 'Y': 0.7231032252311707}, {'Type': 'midJawlineRight', 'X': 0.9120021421701915, 'Y': 0.111412505259375}, {'Type': 'upperJawlineRight', 'X': 0.9241121100959772, 'Y': 0.5102249721902519}], 'Pose': {'Roll': -3.4002102100372314, 'Yaw': 0.31129127547123711, 'Pitch': 12.01332772930114}, 'Quality': {'Brightness': 12.41993713372901, 'Sharpness': 53.330047107421275}, 'Confidence': 99.99993133544922}]}
    res = rekognition_data_formatter.format_analysis_log_data(json.dumps(analysis_data))
    

if __name__ == "__main__":
    # 認証ログデータ加工のテスト用
    test_call_format_auth_log_data()
    # 顔画像分析データ加工のテスト用
    test_call_format_analysis_log_data()