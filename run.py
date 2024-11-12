from UPISAS.strategies.swim_reactive_strategy import ReactiveAdaptationManager
from UPISAS.strategies.empty_strategy import EmptyStrategy
from UPISAS.exemplar import Exemplar
from UPISAS.exemplars.dingnet import Dingnet
import signal
import sys
import time

if __name__ == '__main__':
    
    exemplar = Dingnet(auto_start=True)
    time.sleep(20)
    exemplar.start_run()
    time.sleep(3)

    try:
        strategy = EmptyStrategy(exemplar)

        strategy.get_monitor_schema()
        strategy.get_adaptation_options_schema()
        strategy.get_execute_schema()

        while True:
            input("Try to adapt?")
            strategy.monitor(verbose=True)
            if strategy.analyze():
                if strategy.plan():
                    strategy.execute()
            
    except (Exception, KeyboardInterrupt) as e:
        print(str(e))
        input("something went wrong")
        exemplar.stop_container()
        sys.exit(0)