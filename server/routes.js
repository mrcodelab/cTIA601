// configure routes
app.config(function ($routeProvider) {
    $routeProvider
        .when("/", { 
            template: "index.html" 
        })
        .when("/cryptography", { 
            templateUrl: "Domain1_Attacks-Threats-Vulns/Cryptography.html",
            controller: 'CryptographyController'
        })
        .when("/risk_mgmt", { 
            templateUrl: "Domain1_Attacks-Threats-Vulns/RiskManagement.html"
        })
        .when("/RMF-0", { 
            templateUrl: "NIST_DoD_RMF/RMF_Phases/P0_Sec_Auth_Process.html" 
        })
        .when("/RMF-1", { 
            templateUrl: "NIST_DoD_RMF/RMF_Phases/P1_Categorization.html" 
        })
        .when("/RMF-2", { 
            templateUrl: "NIST_DoD_RMF/RMF_Phases/P2_Select.html" 
        })
        .when("/RMF-3", { 
            templateUrl: "NIST_DoD_RMF/RMF_Phases/P3_Implement.html" 
        })
        .when("/RMF-4", { 
            templateUrl: "NIST_DoD_RMF/RMF_Phases/P4_Assess.html" 
        })
        .when("/RMF-5", { 
            templateUrl: "NIST_DoD_RMF/RMF_Phases/P5_Authorize.html" 
        })
        .when("/RMF-6", { 
            templateUrl: "NIST_DoD_RMF/RMF_Phases/P6_Monitor-Decom.html" 
        })
});