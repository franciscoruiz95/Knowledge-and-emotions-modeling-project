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
		'p_init'	: 0.45805,
		'p_guess'	: 0.588011,
		'p_slip'	: 0.07399,
		'p_transit'	: 0.053606,
	},
	2 : {
		'p_init'	: 0.126253,
		'p_guess'	: 0.392545,
		'p_slip'	: 0.00477,
		'p_transit'	: 0.104403,
	},
	3 : {
		'p_init'	: 0.165781,
		'p_guess'	: 0.143285,
		'p_slip'	: 0.168365,
		'p_transit'	: 0.000192,
	},
	4 : {
		'p_init'	: 0.141083,
		'p_guess'	: 0.360573,
		'p_slip'	: 0.000999,
		'p_transit'	: 0.057817,
	},
	5 : {
		'p_init'	: 0.13698,
		'p_guess'	: 0.412585,
		'p_slip'	: 0.005846,
		'p_transit'	: 0.057484,
	},
}