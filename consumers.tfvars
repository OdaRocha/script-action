{
    consumers : [
        {
            path: "path_orquestrador",
            controle_acesso: [
                {
                    api_key: "52c2d78a-b1d9-4000-8cc3-bf11dcd4e0f9"    
                    nome: "API_KEY_1"
                    throttling : [
                        {
                            method : null
                            tps: 10
                        }
                    ]    
                },
                {
                    api_key: "96308b9d-b7f8-4ca8-a500-dba0e6efba71"    
                    nome: "API_KEY_2"
                    throttling : [
                        {
                            method : get
                            tps: 10
                        },
                        {
                            method : null
                            tps: 0
                        }
                    ]    
                },
                {
                    api_key: "21577a4a-62dd-459a-8f48-6601b588e028"    
                    nome: "API_KEY_3"
                    throttling : [
                        {
                            method : null
                            tps: 10
                        }
                    ]    
                },
                {
                    api_key: "768d615d-10a2-4d18-8794-0441b8367575"    
                    nome: "API_KEY_4"
                    throttling : [
                        {
                            method : post
                            tps: 10
                        },
                        {
                            method : null
                            tps: 0
                        }
                    ]    
                }
            ]
        }
    ]
}