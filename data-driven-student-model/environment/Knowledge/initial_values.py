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
		'p_init'	: 0.712684,
		'p_guess'	: 0.621497,
		'p_slip'	: 0.200791,
		'p_transit'	: 0.186808,
	},
	2 : {
		'p_init'	: 0.129854,
		'p_guess'	: 0.356858,
		'p_slip'	: 0.051951,
		'p_transit'	: 0.161936,
	},
	3 : {
		'p_init'	: 0.198238,
		'p_guess'	: 0.168163,
		'p_slip'	: 0.179856,
		'p_transit'	: 0.002052,
	},
	4 : {
		'p_init'	: 0.501916,
		'p_guess'	: 0.358944,
		'p_slip'	: 0.184713,
		'p_transit'	: 0.076271,
	},
	5 : {
		'p_init'	: 0.468174,
		'p_guess'	: 0.340405,
		'p_slip'	: 0.170732,
		'p_transit'	: 0.052269,
	},
}