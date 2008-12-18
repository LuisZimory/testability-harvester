// Copyright 2008 Google, Inc. All Rights Reserved.
package com.google.testing.harvester {
  import mx.collections.ArrayCollection;
  import mx.controls.Alert;
  import mx.rpc.events.FaultEvent;
  import mx.rpc.events.ResultEvent;
  import mx.rpc.http.HTTPService;
  import mx.utils.StringUtil;
  
  /**
   * @author Misko Hevery <misko@google.com>
   */
  public class Server {
    
    private var URL_DATA:String = "http://www.corp.google.com/~harvester/harvester.php";
    private var URL_PROJECTS:String = "http://www.corp.google.com/~harvester/projects_2.php";
    
    public function fetchProjects(callback:Function):void {
      var service:HTTPService = new HTTPService();
      service.url = URL_PROJECTS;
      service.resultFormat = HTTPService.RESULT_FORMAT_TEXT;
      service.addEventListener(ResultEvent.RESULT, 
        function (event:ResultEvent):void {
          callback(new ProjectParser().parseProjects(String(service.lastResult)));
        });
      service.addEventListener(FaultEvent.FAULT, 
        function (event:FaultEvent):void {
          Alert.show(event.toString());
        });
      service.send();
    }

    /**
     * Load data set from web-service for a specific project.
     */
    public function fetchChangelists(name:String, callback:Function):void {
      var httpService:HTTPService = new HTTPService();
      httpService.request = {path:name + ".csv"};
      httpService.url = URL_DATA;
      httpService.addEventListener(ResultEvent.RESULT, 
        function(event:ResultEvent):void {
          callback(new ChangeListParser().parseChangeLists(httpService.lastResult as String));
        });
      httpService.addEventListener(FaultEvent.FAULT, 
        function(event:FaultEvent):void {
          Alert.show(event.toString());
        });
      httpService.send();
    }
    
    public function saveProject(project:Project):void {
      var service:HTTPService = new HTTPService();
      service.url = URL_DATA;
      service.request = {path:project.name + ".info", data:project.toString()};
      service.addEventListener(FaultEvent.FAULT, 
        function (event:FaultEvent):void {
          Alert.show(event.toString());
        });
      service.send();
    }
  }
}