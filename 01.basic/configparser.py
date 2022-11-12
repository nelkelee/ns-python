#설정값등은 하드코딩하지 말고 config parser를 이용하여 따로 파일로 관리하여 사용하자
import configparser

config = configparser.ConfigParser()
config.sections()
config.read('config.py')

print(config['ABC']['A'])
print(config['ABC']['B'])
#print(config['ABC']['C'])
print(config['DEF'])
