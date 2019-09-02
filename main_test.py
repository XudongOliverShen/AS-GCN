import argparse
import sys
import torchlight
from torchlight import import_class


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Processor collection')

    processors = dict()
    processors['recognition'] = import_class('processor.recognition.REC_Processor')
    # processors['demo'] = import_class('processor.demo.Demo')

    subparsers = parser.add_subparsers(dest='processor')
    for k, p in processors.items():
        subparsers.add_parser(k, parents=[p.get_parser()])

    arg = parser.parse_args()
    
    config_path = 'config/as_gcn/ntu-xsub/permutation_test/'
    for method in ['permutate_by_frame', 'permutate_by_clip']:
        if method=='permutate_by_frame':
            for num_frames_per_clip in [10,20,30,40,50]:
                print(method,num_frames_per_clip)
                sys.argv[3] = config_path + method + '_' + str(num_frames_per_clip) + '.yaml'
                Processor = processors[arg.processor]
                p = Processor(sys.argv[2:])
                p.start()
        elif method=='permutate_by_clip':
            for num_clips_per_video in [2,3,4,5,6]:
                print(method, num_clips_per_video)
                sys.argv[3] = config_path + method + '_' + str(num_clips_per_video) + '.yaml'
                Processor = processors[arg.processor]
                p = Processor(sys.argv[2:])
                p.start()
            
