"""
    Valores iniciales para implementar el modelo BKT\skill_n
    initial_values = {skill_n : {\n
            'p_init'    : val_l,\n
            'p_guess'   : val_g,\n
            'p_slip'    : val_s,\n
            'p_transit' : val_t,\n
        },}\n

    Hay 4 parámetros de modelo utilizados en BKT:\n
    p_init,     la probabilidad de que el estudiante conozca la habilidad de antemano.\n
    p_guess,    la probabilidad de que el estudiante aplique correctamente una habilidad desconocida (tiene suerte)\n
    p_slip,     la probabilidad de que el estudiante cometa un error al aplicar una habilidad conocida\n
    p_transit,  la probabilidad de que el estudiante demuestre conocimiento de la habilidad después de una oportunidad de aplicarla
"""
initial_values = {
	1 : {
		'p_init'	: 0.354898,
		'p_guess'	: 0.622988,
		'p_slip'	: 0.002087,
		'p_transit'	: 0.019993,
	},
	2 : {
		'p_init'	: 0.166123,
		'p_guess'	: 0.308424,
		'p_slip'	: 0.014533,
		'p_transit'	: 0.167389,
	},
	3 : {
		'p_init'	: 0.180874,
		'p_guess'	: 0.17726,
		'p_slip'	: 0.175042,
		'p_transit'	: 0.003577,
	},
	4 : {
		'p_init'	: 0.658485,
		'p_guess'	: 0.314347,
		'p_slip'	: 0.211477,
		'p_transit'	: 0.01408,
	},
	5 : {
		'p_init'	: 0.289022,
		'p_guess'	: 0.376097,
		'p_slip'	: 0.080253,
		'p_transit'	: 0.078427,
	},
}