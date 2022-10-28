

import sys
sys.path.append('D:\BotParserFinanceCompany\BotParserFinanceCompany\controller')
sys.path.append('D:\BotParserFinanceCompany\BotParserFinanceCompany\controller\command')
sys.path.append('D:\BotParserFinanceCompany\BotParserFinanceCompany\model')
sys.path.append('D:\BotParserFinanceCompany\BotParserFinanceCompany\model\companyModel')
sys.path.append('D:\BotParserFinanceCompany\BotParserFinanceCompany\\view')
print(sys.path)

from controller.controllerTelegram import ControllerTelegram
botOrganazier = ControllerTelegram()
botOrganazier.start_bot()