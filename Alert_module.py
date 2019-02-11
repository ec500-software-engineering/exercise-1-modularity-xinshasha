#copyright @Xinsha Wang
#It's the I/O documentation for Alert System
#Alert Sys
class Alert():
    def __init__(self):
        self.fine_turn = 0
        self.bo_flag = 0
        self.bp_flag = 0
        self.pul_flag = 0

    def get_bo_data(self,data):
        if self.fine_turn > 20:
            self.bo_flag = 0
        if 0 <= data <= 0.3:
            self.bo_flag += 1
        else:
            self.fine_turn += 1

    def get_bp_data(self,data):
        if self.fine_turn > 20:
            self.bp_flag = 0
        if 60<= data <= 90:
            self.bp_flag += 1
        else:
            self.fine_turn += 1 

    def get_pul_data(self,data):
        if self.fine_turn > 20:
            self.pul_flag = 0
        if 90 <= data <=120:
            self.pul_flag += 1
        else:
            self.fine_turn += 1


    def Alert_Output(self):
        """
        Compare data with certain threthold
        send flags to user interface module.
        """
        if self.bo_flag != 0:
            return 1
        elif self.bp_flag != 0:
            return 2
        elif self.pul_flag != 0:
            return 3
        else:
            return 0