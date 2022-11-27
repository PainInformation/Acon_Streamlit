from data import timeseries_module as tm

def tk():
        #paths = './drive/MyDrive/data/'
        paths = './data/tem/'

        file_list_dict = tm.get_filelist(paths)

        #print(file_list_dict)

        data = tm.get_data(file_list_dict['MI'])

        #print(data)

        m_data = {}
        for key, value in data.items():
                df = tm.missing_check(value, 'T')
                df = tm.physical_check(df)
                df = tm.step_check1(df)
                #print(df)
                df = tm.persistence_check(df)
                key_f = tm.keep_data(df)
                m_data[key_f] = df

        hourly = tm.resample_hour(m_data)
        tm.keep_data(hourly, 'OBS_108_AirTemp_hourly_data') 
        diurnal = tm.resample_day(hourly)
        tm.keep_data(diurnal,'OBS_108_AirTemp_diurnal_data')

        h_data = tm.get_data(file_list_dict['TIM'])

        for i in h_data:
                df = h_data[i]
                df = tm.resample_day(df,'temp') 
                tm.keep_data(df, 'OBS_108_AirTemp_2021_data')

        df_month = tm.resample_month(df)
        tm.keep_data(df_month, 'OBS_108_AirTemp_month_data')
        #print(df_month)

        #tm.timeseries_plot(df)
