import Input_Module_lkn
import storage
import Alert_module
import AiModule
import UserInterface_module
#Input
bo = Input_Module_lkn.read_data('./bo.txt')
bp = Input_Module_lkn.read_data('./bp.txt')
pul = Input_Module_lkn.read_data('./pulse.txt')
#Store
data = []
for i in range(len(bo)):
	t=storage.storage(bo[i],bp[i],pul[i])
	data.append(t)
#Alert
alert_sys = Alert_module.Alert()
for i in data:
	alert_sys.get_bo_data(i.read('bo'))
	alert_sys.get_bp_data(i.read('bp'))
	alert_sys.get_pul_data(i.read('pul'))
UserInterface_module.alert_out(alert_sys.Alert_Output())
#AI
ai = AiModule.AiModule()
ai.input_check(bo,bp,pul)
pbo,pbp,ppul=ai.predict()
UserInterface_module.ai_output(pbo,pbp,ppul)


	



